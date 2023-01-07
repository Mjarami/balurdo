import os
import datetime
from tkinter import *
from tkinter import filedialog
import subprocess

def tiempo_global():
    tiempo = globals()['tiempo'].replace(" ","")
    return tiempo

def crea_ventana():
    def devolverDatos():
        globals()['tiempo'] = "{}".format(tiempo.get())
        escribe()
    def variable_directorio():
        directorio_text = filedialog.askdirectory()
        globals()['directorio'] = directorio_text
    ventana = Tk()
    ventana.title("Balurdo")
    vp = Frame() #Creacion del Frame
    vp.pack()  #Empaquetamiento del Frame
    ##vp.config(bg="blue") #cambiar color de fondo 
    ##vp.config(width="400", height="200") #cambiar tamaño
    vp.config(bd=5) #cambiar el grosor del borde
    vp.config(relief="sunken")   #cambiar el tipo de borde
    ##vp.config(cursor="heart")    #cambiar el tipo de cursor
    etiqueta0 = Label(vp, text="Bienvenido!!!...")
    etiqueta0.grid(column=2, row=3, sticky=(W,E))
    etiqueta1 = Label(vp, text="")
    etiqueta1.grid(column=3, row=3, sticky=(W,E))
    etiqueta2 = Label(vp, text="Directorio:")
    etiqueta2.grid(column=2, row=4, sticky=(W,E))
    cargar = Button(vp, text="Buscar", command=variable_directorio)
    cargar.grid(column=3, row=4)
    etiqueta3 = Label(vp, text="Tiempo:")
    etiqueta3.grid(column=2, row=5, sticky=(W,E))
    tiempo = Entry(vp, width=5)
    tiempo.grid(column=3, row=5)
    boton = Button(vp, text="Guardar", command=devolverDatos)
    boton.grid(column=2, row=6)
    boton = Button(vp, text="Cerrar", command=ventana.destroy)
    boton.grid(column=3, row=6)
    ventana.mainloop()

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
        documento += "\t<static>\n\t\t<duration>"+tiempo+"</duration>\n\t\t<file>"+globals()['directorio']+"/"+v1+"</file>\n\t</static>\n"
        documento += "\t<transition>\n\t\t<duration>0.5</duration>\n\t\t<from>"+globals()['directorio']+"/"+v1+"</from>\n"
        documento += "\t\t<to>"+globals()['directorio']+"/"+v2+"</to>\n\t</transition>\n"
    final = "</background>"
    escribe = documento+final
    return escribe

def escribe():
    ## Se genera el archivo lista-imagenes
    directorio = globals()['directorio'].replace(" ","")
    result = subprocess.run(["ls", directorio], capture_output=True, text=True)
    crea_procesando = subprocess.run(["mkdir", ""+os.getcwd()+"/procesando"])
    crea_xml = subprocess.run(["mkdir", ""+os.getcwd()+"/xml"])
    archivo = gestiona_archivo(os.getcwd()+'/procesando/lista-imagenes.txt','w', result.stdout)
    ## Se cargan las imagenes leyendo el archivo .txt
    archivo = gestiona_archivo(os.getcwd()+'/procesando/lista-imagenes.txt', 'r', "")
    lista = gestiona_cadena(archivo)
    ## Se procede a estructurar el documento .xml con la lista de imagenes
    escribe = gestiona_xml(lista)
    ## Se crea el documento .xml
    archivo = gestiona_archivo(os.getcwd()+'/xml/fondo.xml','w', escribe)

crea_ventana()

