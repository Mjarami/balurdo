import os
import datetime
from tkinter import *
from tkinter import filedialog
import subprocess

def tiempo_global():
    tiempo = globals()['tiempo'].replace(" ","")
    if tiempo == None or tiempo == "":
        tiempo = "300"
    archivo = gestiona_archivo(os.getcwd()+'/procesando/tiempo.txt','w', tiempo)
    return tiempo

def crea_ventana():
    def devolverDatos():
        globals()['tiempo'] = tiempo.get()
        escribe()
    def variable_directorio():
        directorio_text = filedialog.askdirectory()
        archivo = gestiona_archivo(os.getcwd()+'/procesando/directorio.txt','w', directorio_text)
        globals()['directorio'] = directorio_text
    def variable_xml():
        dir_xml = filename = filedialog.asksaveasfilename(
            filetypes=(
                ("Archivos xml", "*.xml"),
            )
        )
        globals()['dir_xml'] = dir_xml
    ventana = Tk()
    ventana.title("F-D-C")
    vp = Frame() #Creacion del Frame
    vp.pack()  #Empaquetamiento del Frame
    ##vp.config(bg="blue") #cambiar color de fondo 
    ##vp.config(width="400", height="200") #cambiar tamaño
    vp.config(bd=6) #cambiar el grosor del borde
    vp.config(relief="sunken")   #cambiar el tipo de borde
    ##vp.config(cursor="heart")    #cambiar el tipo de cursor
    etiqueta0 = Label(vp, text="Welcome!!!...")
    etiqueta0.grid(column=2, row=3, sticky=(W,E))
    etiqueta1 = Label(vp, text="")
    etiqueta1.grid(column=3, row=3, sticky=(W,E))
    etiqueta3 = Label(vp, text="File")
    etiqueta3.grid(column=3, row=4, sticky=(W,E))
    directorio_anterior = gestiona_archivo(os.getcwd()+'/procesando/directorio.txt', 'r', "")
    etiqueta5 = Label(vp, text=directorio_anterior)
    etiqueta5.grid(column=2, row=5, sticky=(W,E))
    etiqueta6 = Label(vp, text="<--- Directory --->")
    etiqueta6.grid(column=3, row=5, sticky=(W,E))
    globals()['directorio'] = ""
    cargar = Button(vp, text="New", command=variable_directorio)
    cargar.grid(column=4, row=5)
    tiempo_anterior = gestiona_archivo(os.getcwd()+'/procesando/tiempo.txt', 'r', "")
    etiqueta7 = Label(vp, text=tiempo_anterior+" Seg")
    etiqueta7.grid(column=2, row=6, sticky=(W,E))
    etiqueta8 = Label(vp, text="<--- Time --->")
    etiqueta8.grid(column=3, row=6, sticky=(W,E))
    tiempo = Entry(vp, width=5)
    tiempo.grid(column=4, row=6)
    xml_anterior = gestiona_archivo(os.getcwd()+'/procesando/xml.txt', 'r', "")
    globals()['xml_anterior'] = xml_anterior
    etiqueta9 = Label(vp, text=xml_anterior)
    etiqueta9.grid(column=2, row=7, sticky=(W,E))
    etiqueta10 = Label(vp, text="<--- XML --->")
    etiqueta10.grid(column=3, row=7, sticky=(W,E))
    globals()['dir_xml'] = ""
    boton = Button(vp, text="New", command=variable_xml)
    boton.grid(column=4, row=7)
    etiqueta11 = Label(vp, text="<--- Feh --->")
    etiqueta11.grid(column=3, row=8, sticky=(W,E))
    boton = Button(vp, text="Go", command=feh_aleatorio)
    boton.grid(column=4, row=8)
    boton = Button(vp, text="Save", command=devolverDatos)
    boton.grid(column=2, row=8)
    ##boton = Button(vp, text="Close", command=ventana.destroy)
    ##boton.grid(column=5, row=9)
    ventana.mainloop()

def gestiona_archivo(ubicacion, proceso, edita):
    f = open (ubicacion, proceso)
    if proceso == 'a' or proceso == 'w':
        gestiona= f.write(edita)
    else:
        gestiona = f.read()
    f.close()
    return gestiona

def feh_aleatorio():
    inicia_fondo = subprocess.run(["./start2.sh"])
    
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
    tiempo = "{}".format(tiempo)
    for v1,v2 in zip(lista,lista2):
        documento += "\t<static>\n\t\t<duration>"+tiempo+"</duration>\n\t\t<file>"+globals()['directorio']+"/"+v1+"</file>\n\t</static>\n"
        documento += "\t<transition>\n\t\t<duration>0.5</duration>\n\t\t<from>"+globals()['directorio']+"/"+v1+"</from>\n"
        documento += "\t\t<to>"+globals()['directorio']+"/"+v2+"</to>\n\t</transition>\n"
    final = "</background>"
    escribe = documento+final
    return escribe

def escribe():
    ## Se genera el archivo lista-imagenes
    if globals()['directorio'] == None or globals()['directorio'] == "":
        directorio = gestiona_archivo(os.getcwd()+'/procesando/directorio.txt', 'r', "")
        globals()['directorio'] = directorio
    else:
        directorio = globals()['directorio'].replace(" ","")
        globals()['directorio'] = directorio
    result = subprocess.run(["ls", directorio], capture_output=True, text=True)
    crea_procesando = subprocess.run(["mkdir", ""+os.getcwd()+"/procesando"])
    crea_xml = subprocess.run(["mkdir", ""+os.getcwd()+"/xml"])
    archivo = gestiona_archivo(os.getcwd()+'/procesando/lista-imagenes.txt','w', result.stdout)
    ## Se cargan las imagenes leyendo el archivo .txt
    archivo = gestiona_archivo(os.getcwd()+'/procesando/lista-imagenes.txt', 'r', "")
    lista = gestiona_cadena(archivo)
    globals()['lista-procesada'] = lista
    ## Se procede a estructurar el documento .xml con la lista de imagenes
    escribe = gestiona_xml(lista)
    ## Se crea el documento .xml
    dir_xml = globals()['dir_xml'].replace(" ","")
    xml_anterior = globals()['xml_anterior'].replace(" ", "")
    if dir_xml == None or dir_xml == "":
        if xml_anterior == None or xml_anterior == "":
            dir_xml = os.getcwd()+"/xml/fondos.xml"
        else:
            dir_xml = xml_anterior
    archivo = gestiona_archivo(os.getcwd()+'/procesando/xml.txt','w', dir_xml)
    archivo = gestiona_archivo(dir_xml,'w', escribe)
    actualiza = subprocess.run(["./start.sh"])

crea_ventana()

