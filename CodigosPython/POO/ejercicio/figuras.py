##Figura, Rectangulo, Circulo y la función probar_figura.
import math

class Figura(object):
    def __init__(self,nombre):
        self.nombre=nombre

    def area(self):
        pass

    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
    def area(self):
        salida=self.base *self.altura
        print(f'El área es: {salida}')
    def perimetro(self):
        salida=2*(self.base+self.altura)
        print(f'El Perimetro es: {salida}')

class Circulo(Figura):
    def __init__(self,nombre,radio):
        super().__init__(nombre)
        self.radio=radio
       
    def area(self):
        salida=math.pi*(self.radio**2)
        print(f'El área es: {salida}')
    def perimetro(self):
        salida=2*math.pi*self.radio
        print(f'El Perimetro es: {salida}')


def probar_figura(object):
    attrs = vars(object)
    print(', '.join("%s: %s" % item for item in attrs.items()))
    object.area()
    object.perimetro()

