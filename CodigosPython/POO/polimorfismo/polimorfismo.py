class Persona(object):
    def __init__(self,nombre):
        self.nombre=nombre

    def moverse(self):
        print('Ando Caminando')


class Atleta(Persona):

    def moverse(self):
        print('ando Corriendo')

class Ciclista(Persona):

    def moverse(self):
        print('ando en bici')