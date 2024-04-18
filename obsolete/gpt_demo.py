from transformers import GPT2Tokenizer, GPT2LMHeadModel

def generate_text(prompt, model_name='gpt2', max_length=100):
    # Load pre-trained model and tokenizer
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)

    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors='pt')

    # Generate text
    output = model.generate(input_ids,
                            max_length=100,
                            num_return_sequences=1,
                            temperature=1.5,
                            top_k=40,
                            top_p=0.9,
                            repetition_penalty=1.2)

    # Decode and print the generated text
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)
    print(generated_text)

# Example prompt
prompt = "How do you live properly?"
generate_text(prompt)
