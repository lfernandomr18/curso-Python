valores=[]
dicc={}
cantValores=int(input('Ingrese cantitad de valores a ingresar: '))



for i in range(cantValores):
    valores.append(input('Ingrese valor: '))
    dicc[input('Ingrese una llave: ')]=input('Ingrese un Valor:')
print(valores)
print(dicc)



