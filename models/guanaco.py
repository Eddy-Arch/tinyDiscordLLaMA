from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained('./weights/guanaco.bin', model_type='llama', gpu_layers=150)

def generate_from_model(prompt):
    for text in llm(prompt, stream=True):
        return text
