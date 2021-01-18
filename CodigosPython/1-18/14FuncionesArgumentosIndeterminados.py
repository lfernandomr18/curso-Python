
## de esta forma se envia  NUMERO INDETERMINADOS DE ARGUMENTOS
def ejemplo1(*args):
    print(args)

ejemplo1(1,2,3)

##DE ESTA FORMA SE ENVIA ARGUMENTOS CON SU KEY Y RETORNA COMO DICCIONARIO

def ejemplo2(**kwargs):
    print(kwargs)
ejemplo2(a=1,b=2,c=3)