class ExcptnEjm(Exception):
    def __init__(self,mensaje):
        super().__init__(mensaje)


error=1
while (error==1):
    try:
        a=int(input('ingrese dividendo:'))
        b=int(input('ingrese Divisor:'))
        
            

        divi=a/b
        print(f'divi:{divi}')
        error=0
    except ZeroDivisionError:
        raise ExcptnEjm('No se puede dividir por cero causa')
    except ValueError:
        raise ExcptnEjm('Solo se permite enteros que pasa causa')
    except Exception as error:
        print('ha ocurrido un error:',type(error).__name__)