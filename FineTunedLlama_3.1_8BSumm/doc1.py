from transformers import AutoTokenizer, AutoModelForCausalLM
from textos import jud_text, jud_text133kb, test
import time

# Cargar el modelo y el tokenizador
model_name = "raaec/Meta-Llama-3.1-8B-Instruct-Summarizer"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)


inputs = tokenizer(jud_text, return_tensors="pt")


print("Comienza generación de resumen...")
start_time = time.time()
# Generar el resumen usando `generate`
summary_ids = model.generate(inputs['input_ids'], 
                             attention_mask=inputs['attention_mask'],
                             pad_token_id=tokenizer.eos_token_id,  # Definir explícitamente el pad_token_id
                             max_new_tokens=400, 
                             min_new_tokens=40, 
                             length_penalty=2.0, 
                             num_beams=2, 
                             early_stopping=True)

print(summary_ids)
print(len(summary_ids))

# Decodificar el resumen generado
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

print(f"Se tardó {(time.time() - start_time)/60} minutos en generar el resumen.")
print(summary)


