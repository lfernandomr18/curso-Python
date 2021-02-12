from figuras import Circulo,Rectangulo,probar_figura

def main():
    while(True):
        print('****************************************************')
        print('         AREA Y PERIMETRO DE FIGURAS GEOMETRICAS')
        print('1 - Rectangurlo')
        print('2 - Circulo')
        print('3 - Salir')
        opcion=int(input('ingrese una opcion :'))
        print('****************************************************')

        if(opcion>2):
            break
        elif(opcion==1):
            base=float(input('Ingrese la base:'))
            altura=float(input('Ingrese la altura:'))
            rect=Rectangulo('Rectangulo',base,altura)
            probar_figura(rect)
            input('presiona enter para continuar....')
        elif(opcion==2):
            radio=float(input('Ingrese el radio:'))
            circ=Circulo('Circulo',radio)
            probar_figura(circ)
            input('presiona enter para continuar....')
     
       
        

main()