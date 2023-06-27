from ctransformers import AutoModelForCausalLM

llm = AutoModelForCausalLM.from_pretrained('./weights/llama.bin', model_type='llama', max_new_tokens=40, gpu_layers=150)

def generate_from_model(prompt):

    for text in llm(prompt, stream=True):
        return text
