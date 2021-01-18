
texto="  Hola Mundo esto es fernando  "


##DEVUELVE LA CADENA EN MAYUSCULA
print(texto.upper())

## todo a minuscula
print(texto.lower())
##primer caractert en mayuscula
print(texto.capitalize())
## primer caracter de cada palabra en mayuscula
print(texto.title())
## contar una subcadena dentro de una cadena
print(texto.count("e"))
##find busca en que indide comienza una subcadena
print(texto.find("Mundo"))
## busca en que indice esta la subcadena desde el final
print(texto.rfind("Hola Mundo"))
##verifica si es numero
print(texto.isdigit())
##verifica si tiene solo numero y alfabetico (false si tiene espacios)
print(texto.isalnum())
## true si todo es alfabeticos (false si tiene espacios)
print(texto.isalpha())

## true si todo es minusculas
print(texto.islower())
## true si todo es mayusculas
print(texto.isupper())
##true si la primera letra de cada palabra es mayuscula
print(texto.istitle())
##true si todo la cadena es espacios
print(texto.isspace())

## true si la cadena empieza con subcadena
print(texto.startswith("Hola"))
## true si la cadena termina con subcadena
print(texto.endswith("Hola"))
##split
print(texto.split())
##une todos los caracteres de una cadena por un  caracter definido
print("-".join(texto))
##borra todos los espacios por delante y detras de una cadena
print(texto.strip())
##reemplaza caracteres por otros
print(texto.replace('o','0'))