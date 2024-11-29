import re
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from textos import jud_text, jud_text133kb, jud_text103kb


WHITESPACE_HANDLER = lambda k: re.sub('\s+', ' ', re.sub('\n+', ' ', k.strip()))

model_name = "csebuetnlp/mT5_multilingual_XLSum"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

input_ids = tokenizer(
    text=[WHITESPACE_HANDLER(jud_text103kb)],
    return_tensors="pt",
    padding=True,
    truncation=False
)["input_ids"]

output_ids = model.generate(
    input_ids=input_ids,
    min_length=512,
    max_length=612,
    do_sample=True,
    no_repeat_ngram_size=2,
    num_beams=8,
    top_p=0.8,
    top_k=50,
    renormalize_logits=True
)[0]

summary = tokenizer.decode(
    output_ids,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(summary)
