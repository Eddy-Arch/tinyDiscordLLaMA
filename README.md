# discordLLM - Running Large Language Models locally through discord
This repo allows you to chat with large language models, locally,
through the comfortable Discord interface.
![Screenshot](https://cdn.discordapp.com/attachments/873898434950746145/1122165476571742228/image.png)

## Available models
Currently, you can talk to an *uncensored* version of the following models:

- Falcon (7B parameters) (GGML 4Bit Quantization) (Uncensored)
- LLaMA (7B parameters) (GGML 4Bit Quantization)
- Vicuna (7B parameters) (GGML 4Bit Quantization) (Uncensored)

## Getting started:
To begin using the model, you must download the weights
for it. I have included a handy script that will automatically
download the weights from HuggingFace.

Lets say i want to use the LLaMA model.
```bash
chmod +x prepare_llama.sh
bash ./prepare_llama.sh
```
then you must install the required dependencies for this to run.
```bash
pip3 install -r requirements.txt
```
Next, you must create a discord Developer application, and pass
your token in the config.py file.
then you must make sure to have selected the model you have installed.
Then, you may run the following command to start the bot
```bash
python3 bot.py
```
## Usage:
Commands must be executed with a prefix, the default prefix is "!"
There are 3 available commands:
- generate "a story about a beautiful butterfly" - generates the output 
- stop - stops generation
- model - lists which model is currently being used for text generation

## How is this possible?
Heres a writeup on my blog:
