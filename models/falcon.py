from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained('./weights/falcon.bin', model_type='falcon')

def generate(prompt):
    yield prompt + "\n"
    for text in llm(prompt, stream=True):
        yield text

def generate_from_model(prompt):
    generated_text = ""
    generator = generate(prompt)
    for text in generator:
        generated_text += text
        print(text, end="", flush=True)
    return generated_text
