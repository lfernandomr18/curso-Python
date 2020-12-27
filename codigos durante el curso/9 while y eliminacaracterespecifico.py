numero=int(input('Ingresa un número: '))
textosalida=''

def kill_char(string, n): # n = position of which character you want to remove
    begin = string[:n]    # from beginning to n (n not included)
    end = string[n+1:]    # n+1 through end of string
    return begin + end
# print kill_char("EXAMPLE", 3)  # "M" removed

if numero >20:
    print('No seas pendejo numero es muy alto...')
else:
    while numero>0:
        textosalida=textosalida+str(numero)+','
        numero=numero-1
numero=len(textosalida)-1#aca retorno la cantidad de caracteres del string
print (kill_char(textosalida,numero))# imprimo la salida con una coma menos