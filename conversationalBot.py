from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

def chat(input_text, philo):
    # Load pre-trained model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-large")
    model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-large")
    input_text = input_text[0]
    # Tokenize input text
    input_ids = tokenizer.encode(input_text + tokenizer.eos_token, return_tensors="pt")

    # Generate response
    output_ids = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)

    # Decode response
    response = tokenizer.decode(output_ids[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    print(response)
    return(response)