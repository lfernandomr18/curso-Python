error=1
while (error==1):
    try:
        a=int(input('ingrese dividendo:'))
        b=int(input('ingrese Divisor:'))

        divi=a/b
        error=0
    except ZeroDivisionError:
        print('debe ingresar un divisor mayor a cero')
    except ValueError:
        print('Solo ingrese numeros enteros')
    

        
    
   
