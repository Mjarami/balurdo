#!/bin/sh
    python3 $(pwd)/proceso1.py
    ls $(cat directorio.txt)/*.jpg > $(cat directorio2.txt)/lista-imagenes.txt
    python3 $(pwd)/proceso2.py