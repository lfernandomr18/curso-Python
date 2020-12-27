# 1. Problema 01: Dado dos números, hallar las suma, resta, división y multiplicación.

# Análisis: Para la solución de este problema, se requiere que ingrese dos números
#  por teclado y el sistema realice el cálculo respectivo para hallar la suma, resta, división y multiplicación.
###############################################################
# a=int(input('ingrese un numero:'))
# b=int(input('ingrese otro numero:'))

# print('la suma es:'+str(a+b))
# print('la resta es:'+str(a-b))
# print('la divisiones:'+str(a/b))
# print('la multiplicacion es:'+str(a*b))
# ###############################################################

# # 2. Problema 02: Hallar el cociente y residuo (resto) de dos números enteros.

# # Análisis: Para la solución de este problema, se requiere que ingrese dos números entero por 
# # teclado y el sistema realice el cálculo respectivo para hallar el cociente y residuo.
# ###############################################################
# a=int(input('ingrese un numero:'))
# b=int(input('ingrese otro numero:'))
# #esto es una funcion para obtener el cociente y residuo de una
# cociente,residuo=divmod(a, b)

# print('El cociente es:'+str(cociente))
# print('El residuo  es:'+str(residuo))
# ###############################################################


# # 3. Problema 03: Dado el valor de venta de un producto, hallar el IGV (18%) y el precio de venta.

# # Análisis: Para la solución de este problema, se requiere que usuario ingrese el valor de venta del producto por teclado y 
# # el sistema realice el cálculo respectivo para hallar el IGV y el precio de venta.
# ###############################################################
a=int(input('ingrese el valor de la venta:'))
igv=a*0.18
venta=igv+a

print('El IGV es:'+str(igv))
print('El valor de la venta  es:'+str(venta))



# ###############################################################