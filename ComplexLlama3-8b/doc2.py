from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch
from accelerate import load_checkpoint_and_dispatch
import os
import time

from textos import jud_text, jud_text103kb, jud_text133kb

os.environ['PYTORCH_CUDA_ALLOC_CONF'] = 'expandable_segments:True'

torch.cuda.empty_cache()

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained("SweatyCrayfish/llama-3-8b-quantized")

# Create a BitsAndBytesConfig for 4-bit quantization
quantization_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16
)

# Load the model with the BitsAndBytesConfig
model = AutoModelForCausalLM.from_pretrained(
    "SweatyCrayfish/llama-3-8b-quantized",
    quantization_config=quantization_config,
    device_map="auto"
)

start_time=time.time()

def generate_summary(text, model, tokenizer, max_length=150, min_length=100, num_beams=4):
    """
    Generates a summary using the LlamaForCausalLM model.
    
    Parameters:
    - text (str): Input text to summarize
    - model: The pre-trained language model
    - tokenizer: The tokenizer for the model
    - max_length (int): Maximum length of the summary
    - min_length (int): Minimum length of the summary
    - num_beams (int): Beam search parameter for more coherent text
    
    Returns:
    - summary (str): The generated summary
    """
    
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512).to("cuda")
    
    # Ensure pad_token_id is different from eos_token_id
    pad_token_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
    
    # Add attention mask to inform model about real tokens vs padding
    attention_mask = inputs['attention_mask']

    # Generate summary
    summary_ids = model.generate(
        inputs["input_ids"],
        attention_mask=attention_mask,
        max_new_tokens=max_length,
        min_new_tokens=min_length,
        num_beams=num_beams,
        length_penalty=2.0,
        early_stopping=True,
        no_repeat_ngram_size=3,
        pad_token_id=pad_token_id  # Set pad token explicitly
    )
    
    # Decode the summary and return it
    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Chain of Tougth  (CoT)
summary = generate_summary(jud_text, model, tokenizer, max_length=2000, min_length=1800)
print(f"Tokens primer resumen: {len(tokenizer(summary)['input_ids'])}")
summary = generate_summary(summary, model, tokenizer, max_length=1500, min_length=1200)
print(f"Tokens segundo resumen: {len(tokenizer(summary)['input_ids'])}")
summary = generate_summary(summary, model, tokenizer, max_length=800, min_length=600)
print(f"Tokens tercer resumen: {len(tokenizer(summary)['input_ids'])}")
summary = generate_summary(summary, model, tokenizer, max_length=500, min_length=400)
print(f"Tokens cuarto resumen: {len(tokenizer(summary)['input_ids'])}")

finish_time=time.time()

print(summary)

print(f"Se tardó aproximadamente {int(finish_time - start_time)} segundos en generar el resumen")

# jud_text tiene 2836 tokens