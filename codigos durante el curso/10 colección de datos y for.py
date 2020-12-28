
#### lista diferente tipo de datos
datos=[5,5.5,'Hola']

for i in datos:
    print(i,type(i))
print('cantidad de datos dentro de lista :'+str(len(datos)))

datos.append('Actualizado')
print(datos)
print('**********************************************************')
####TUPLAS

datostupla=([1,2,3],3,'hola')
print(datostupla)
print('**********************************************************')
#CONJUNTO#
conjunto={'a','b','c','d',1}
print(conjunto)
print('**********************************************************')
#Diccionario

dicc={1:'One',2:'Two','3':'3'}
print(dicc[1])##imprime ONE
del(dicc[1])##elimina 1 del diccionario
print(dicc)
