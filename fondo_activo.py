import os
import subprocess
import random
import threading
import time

def g_archivo(ubicacion, proceso, edita):
    f = open (ubicacion, proceso)
    if proceso == 'a' or proceso == 'w':
        gestiona= f.write(edita)
    else:
        gestiona = f.read()
    f.close()
    return gestiona

def g_cadena(cadena):
    ## Se transforma la cadena en una lista para poder arreglar el contenido
    cadena = cadena.replace(".png",".png,")
    cadena = cadena.replace(".jpg",".jpg,")
    cadena = cadena.replace(".jpeg",".jpeg,")
    cadena = cadena.replace("\n","")
    cadena=list(cadena)
    cadena.pop()
    ## Se transforma la lista en una cadena
    separador =""
    cadena = separador.join(cadena)
    ## Se procede a finalizar llevando la cadena a un array
    cadena=cadena.split(",")
    return cadena

def feh():
    tiempo = g_archivo(os.getcwd()+'/procesando/tiempo.txt', 'r', "")
    tiempo = int(tiempo)
    directorio = g_archivo(os.getcwd()+'/procesando/directorio.txt', 'r', "")
    lista = g_archivo(os.getcwd()+'/procesando/lista-imagenes.txt', 'r', "")
    lista = g_cadena(lista)
    def timer(timer_runs):
        while timer_runs.is_set():
            fondoaleatorio = random.choice(lista)
            define_fondo = subprocess.run(["feh", "--bg-scale", directorio+"/"+fondoaleatorio])
            time.sleep(tiempo)
    timer_runs = threading.Event()
    timer_runs.set()
    t = threading.Thread(name='cambiando', target=timer, args=(timer_runs,))
    t.start()

feh()