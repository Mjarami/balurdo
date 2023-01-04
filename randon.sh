#!/bin/sh
	cd $HOME/Imágenes/wallpaper/
	echo "" > $HOME/Imágenes/wallpaper/fondo.xml
	ls $HOME/Imágenes/wallpaper/fondo-dinamico/*.jpg > $HOME/Imágenes/wallpaper/lista-imagenes.txt && ls $HOME/Imágenes/wallpaper/fondo-dinamico/*.png >> $HOME/Imágenes/wallpaper/lista-imagenes.txt
	python3 $HOME/Imágenes/wallpaper/proceso1.py

