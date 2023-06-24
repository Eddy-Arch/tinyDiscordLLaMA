#!/bin/sh
wget "https://huggingface.co/TheBloke/LLaMa-7B-GGML/resolve/main/llama-7b.ggmlv3.q4_0.bin"
mv llama-7* weights/llama.bin
