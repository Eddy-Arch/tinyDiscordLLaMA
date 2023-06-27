from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained('./weights/falcon.bin', model_type='falcon')

def generate_from_model(prompt):
    for text in llm(prompt, stream=True):
        return text
