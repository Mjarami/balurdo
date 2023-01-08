#!/bin/sh
    pkill -f proceso.py
    pkill -f fondo_activo.py
    python3 $(pwd)/fondo_activo.py