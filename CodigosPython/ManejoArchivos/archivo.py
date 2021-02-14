from io import open
from os import path


def escribirArchivo():
    archivo=open('texto.txt','w')
    archivo.write('Hola mundo')
    archivo.close()

def leerArchivo():
    if path.isfile('texto.txt'):
        archivo=open('texto.txt','r')
        # textos=archivo.read()
        textos2=archivo.readlines()
        archivo.close()
        # print(textos)
        print(textos2)
    else:
        print('No hay archvo')

def agregarDatosArchivo():
    if path.isfile('texto.txt'):
        archivo=open('texto.txt','a')
        archivo.write('\nMesones Ramirez')
        archivo.close()
    else:
        print('No hay archvo')   


def modificarArchivo():
    if path.isfile('texto.txt'):
        archivo=open('texto.txt','r+')
        texto=archivo.readlines()
        print(texto)
        texto[1]='Mi nombre es : Luis Fernando\n'
        texto[2]='Mi Apellido es : Mesones'
        archivo.seek(0)
        archivo.writelines(texto)
        print(texto)
        archivo.close()
    else:
        print('No hay archvo')   

def eliminarDatosArchivo():
     archivo=open('texto.txt','w')
     archivo.close()
eliminarDatosArchivo()
# leerArchivo()
# escribirArchivo()