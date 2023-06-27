#!/bin/sh
wget "https://huggingface.co/TheBloke/MPT-7B-Instruct-GGML/resolve/main/mpt-7b-instruct.ggmlv3.q4_0.bin"
mv mpt-7b* weights/mpt.bin
