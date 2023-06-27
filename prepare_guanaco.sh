#!/bin/sh
wget "https://huggingface.co/TheBloke/guanaco-7B-GGML/resolve/main/guanaco-7B.ggmlv3.q4_0.bin"
mv guanaco-7B* weights/guanaco.bin
