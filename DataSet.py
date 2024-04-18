from transformers import GPT2Tokenizer


def prepare_dataset(texts, max_length=512):
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    encodings = tokenizer(texts, truncation=True, padding=True, max_length=max_length, return_tensors="pt")

    input_ids = encodings['input_ids']
    attention_masks = encodings['attention_mask']

    return input_ids, attention_masks
