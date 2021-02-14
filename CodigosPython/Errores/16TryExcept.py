error=1




while (error==1):
    try:
        a=int(input('ingrese dividendo:'))
        b=int(input('ingrese Divisor:'))
        
            

        divi=a/b
        print(f'divi:{divi}')
        error=0
    except ZeroDivisionError:
        print('debe ingresar un divisor mayor a cero')
    except ValueError:
        print('Solo ingrese numeros enteros')
    except Exception as error:
        print('ha ocurrido un error:',type(error).__name__)

        
    
   
