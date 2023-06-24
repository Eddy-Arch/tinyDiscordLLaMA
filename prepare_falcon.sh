#!/bin/sh
wget "https://huggingface.co/TheBloke/WizardLM-Uncensored-Falcon-7B-GGML/resolve/main/wizard-falcon-7b.ggmlv3.q4_0.bin"
mv wizard-falcon* weights/falcon.bin
