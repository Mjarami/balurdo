import os
import datetime
from tkinter import *
import shlex, subprocess

def tiempo_global():
    tiempo = globals()['tiempo'].replace(" ","")
    return tiempo

def crea_ventana1():
    ventana = Tk()
    ventana.title("Balurdo")
    etiqueta = Label(ventana, text="Bienvenido, estoy muy contento de que pruebes al 'Balurdo'\n Siente comodo de dejarme tus comentarios y sugerencias\nSin mas preambulo arranquemos")
    boton = Button(ventana, text="OK!!", command=crea_ventana2)
    boton2 = Button(ventana, text="Cerrar", command=ventana.destroy)
    etiqueta.pack()
    boton.pack()
    boton2.pack()
    ventana.mainloop()

def crea_ventana2():
    def devolverDatos():
        globals()['tiempo'] = "{}".format(tiempo.get())
        define_directorio(directorio.get())
    ventana = Tk()
    ventana.title("Data inicial")
    vp = Frame(ventana)
    vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
    vp.columnconfigure(0, weight=1)
    vp.rowconfigure(0, weight=1)
    etiqueta_ejemplo_texto = Label(vp, text="Ejemplo --> ")
    etiqueta_ejemplo_texto.grid(column=2, row=2, sticky=(W,E))
    etiqueta_ejemplo = Label(vp, text=os.getcwd())
    etiqueta_ejemplo.grid(column=3, row=2, sticky=(W,E))
    etiqueta_carpeta = Label(vp, text="Directorio:")
    etiqueta_carpeta.grid(column=2, row=3, sticky=(W,E))
    directorio_string = StringVar()
    directorio = Entry(vp, width=20, textvariable=directorio_string)
    directorio.grid(column=3, row=3)
    etiqueta_tiempo = Label(vp, text="Tiempo:")
    etiqueta_tiempo.grid(column=2, row=4, sticky=(W,E))
    tiempo_string = StringVar()
    tiempo = Entry(vp, width=20, textvariable=tiempo_string)
    tiempo_string.set(tiempo)
    tiempo.grid(column=3, row=4)
    boton = Button(ventana, text="Guardar", command=devolverDatos)
    boton.grid(column=4, row=4)
    boton = Button(ventana, text="Cerrar", command=ventana.destroy)
    boton.grid(column=5, row=4)
    
def define_directorio(directorio):
    actual = os.getcwd()
    archivo = gestiona_archivo(os.getcwd()+'/directorio.txt','w', directorio)
    archivo = gestiona_archivo(os.getcwd()+'/directorio2.txt','w', actual)
    escribe()

def gestiona_archivo(ubicacion, proceso, edita):
    f = open (ubicacion, proceso)
    if proceso == 'a' or proceso == 'w':
        gestiona= f.write(edita)
    else:
        gestiona = f.read()
    f.close()
    return gestiona

def gestiona_cadena(cadena):
    ## Se transforma la cadena en una lista para poder arreglar el contenido
    cadena = cadena.replace(".png",".png,")
    cadena = cadena.replace(".jpg",".jpg,")
    cadena = cadena.replace("\n","")
    cadena=list(cadena)
    cadena.pop()
    ## Se transforma la lista en una cadena
    separador =""
    cadena = separador.join(cadena)
    ## Se procede a finalizar llevando la cadena a un array
    cadena=cadena.split(",")
    return cadena

def gestiona_xml(lista):
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    time = currentDateTime.time()
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    hour = time.strftime("%H")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    documento = "<background>\n\t<starttime>\n\t\t<year>"+year+"</year>\n\t\t"+"<month>"+month+"</month>\n\t\t"+"<day>"+day+"</day>"
    documento += "\n\t\t<hour>"+hour+"</hour>\n\t\t<minute>"+minutes+"</minute>\n\t\t<second>"+seconds+"</second>\n\t</starttime>\n"
    ## Se crea el ciclo en la lista
    lista.append(lista[0])
    ## Se crea la lista de llegada
    lista2 = lista[1:]
    ## Se procede a crear y escribir en el documento .xml
    tiempo = tiempo_global()
    if tiempo == None or tiempo == "":
        tiempo = "300"
    for v1,v2 in zip(lista,lista2):
        documento += "\t<static>\n\t\t<duration>"+tiempo+"</duration>\n\t\t<file>"+v1+"</file>\n\t</static>\n"
        documento += "\t<transition>\n\t\t<duration>5.0</duration>\n\t\t<from>"+v1+"</from>\n"
        documento += "\t\t<to>"+v2+"</to>\n\t</transition>\n"
    final = "</background>"
    escribe = documento+final
    return escribe

def escribe():
    ## Se cargan las imagenes leyendo el archivo .txt
    p1 = subprocess.run(["cat", "directorio.txt"], stdout=subprocess.PIPE)
    dir = p1.stdout
    p2 = subprocess.run("ls", cwd = dir+"/*.jpg", stdout=subprocess.PIPE)
    imagenes = p2.stdout
    archivo = gestiona_archivo(os.getcwd()+'/lista-imagenes.txt','w', imagenes)
    archivo = gestiona_archivo(os.getcwd()+'/lista-imagenes.txt', 'r', "")
    lista = gestiona_cadena(archivo)
    ## Se procede a estructurar el documento .xml con la lista de imagenes
    escribe = gestiona_xml(lista)
    ## Se crea el documento .xml
    archivo = gestiona_archivo(os.getcwd()+'/fondo.xml','a', escribe)

crea_ventana1()

