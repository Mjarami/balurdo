import os
import datetime

def gestiona_archivo(ubicacion, proceso, edita):
    f = open (ubicacion, proceso)
    if proceso == 'a':
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
    tiempo = '300'
    for v1,v2 in zip(lista,lista2):
        documento += "\t<static>\n\t\t<duration>"+tiempo+"</duration>\n\t\t<file>"+v1+"</file>\n\t</static>\n"
        documento += "\t<transition>\n\t\t<duration>5.0</duration>\n\t\t<from>"+v1+"</from>\n"
        documento += "\t\t<to>"+v2+"</to>\n\t</transition>\n"
    final = "</background>"
    escribe = documento+final
    return escribe

def cuerpo():
    ## Se cargan las imagenes leyendo el archivo .txt
    archivo = gestiona_archivo(os.getcwd()+'/lista-imagenes.txt', 'r', "")
    lista = gestiona_cadena(archivo)
    ## Se procede a estructurar el documento .xml con la lista de imagenes
    escribe = gestiona_xml(lista)
    ## Se crea el documento .xml
    archivo = gestiona_archivo(os.getcwd()+'/fondo.xml','a', escribe)

cuerpo()

