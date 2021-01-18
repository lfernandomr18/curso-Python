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
# a=int(input('ingrese el valor de la venta:'))
# igv=a*0.18
# venta=igv+a

# print('El IGV es:'+str(igv))
# print('El valor de la venta  es:'+str(venta))



# ###############################################################

# 1. Problema 01: Dado dos números diferentes, devolver el número
# mayor.
# Análisis: Para la solución de este problema, se requiere que
# ingrese dos números por teclado y el sistema realice el proceso
# de devolver el número mayor.

# a=int(input('Ingrese primer valor: '))
# b=int(input('Ingrese segundo valor: '))

# if(a>b):
#     print("el numero mayor es %d"%(a))
# else:
#     print("el numero mayor es %d"%(b))

# 2. Problema 02: Determinar si un número es positivo, negativo o
# neutro.
# Análisis: Para la solución de este problema, se requiere que
# ingrese un número entero por teclado y el sistema verifique si
# es positivo, neutro o negativo.
# numero=int(input('Ingrese un número: '))

# if numero==0:
#     print('numero neutro')
# elif numero>0:
#     print('número positivo')
# else:
#     print('numero negativo')

# Durante el desarrollo de un pequeño videojuego se te encarga configurar y balancear cada clase de personaje jugable. Partiendo que la estadística base es 2, debes cumplir las siguientes condiciones:

#  El caballero tiene el doble de vida y defensa que un guerrero.

#  El guerrero tiene el doble de ataque y alcance que un caballero.

#  El arquero tiene la misma vida y ataque que un guerrero, pero la mitad de su defensa y el doble de su alcance.

#  Muestra como quedan las propiedades de los tres personajes.

caballero = { 'vida':2, 'ataque':2, 'defensa': 2,'alcance':2 }
guerrero = { 'vida':2, 'ataque':2, 'defensa': 2,'alcance':2 }
arquero = { 'vida':2, 'ataque':2, 'defensa': 2,'alcance':2 }


caballero['vida']=(guerrero['vida']*2)
caballero['defensa']=(guerrero['defensa']*2)
guerrero['ataque']=(caballero['ataque']*2)
guerrero['alcance']=(caballero['alcance']*2)
arquero['vida']=guerrero['vida']
arquero['ataque']=guerrero['ataque']
arquero['defensa']=(guerrero['defensa']/2)
arquero['alcance']=(guerrero['alcance']*2)

print('caballero :'+str(caballero))
print('guerrero :'+str(guerrero))
print('arquero :'+str(arquero))


