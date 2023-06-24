import re
from ctransformers import AutoModelForCausalLM
import string

llm = AutoModelForCausalLM.from_pretrained('./weights/falcon.bin', model_type='falcon', max_new_tokens=40)

def generate_from_model(prompt):
    tokens = llm.tokenize(prompt)
    generated_tokens = llm.generate(tokens)
    current_sentence = []
    prev_word = None

    for token in generated_tokens:
        word = llm.detokenize(token).strip()
        word = re.sub(r"\s+", "", word)  # Remove any spaces within the word

        if word in string.punctuation:
            current_sentence.append(word)
            yield ' '.join(current_sentence).strip()
            current_sentence = []
        else:
            if prev_word is not None and (prev_word.endswith("▁") or word.startswith("▁")):
                current_sentence[-1] += word
            else:
                current_sentence.append(word)

        prev_word = word

    # Remove extra spaces before punctuation marks
    yield ' '.join(current_sentence).strip().replace(" '", "'").replace(" n't", "n't")

#prompt = "Write a song about the war effort in Russia"
#sentences_generator = generate_from_model(prompt)

#for sentence in sentences_generator:
    #print(sentence)
