#!/bin/sh
wget "https://huggingface.co/TheBloke/Wizard-Vicuna-7B-Uncensored-GGML/resolve/main/Wizard-Vicuna-7B-Uncensored.ggmlv3.q4_0.bin"
mv Wizard-Vicuna* weights/vicuna.bin
