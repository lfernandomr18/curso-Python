class Productos:
    def __init__(self,codigo,nombre,precio,descripcion):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.descripcion=descripcion

class Adornos(Productos):
    ## esto hace heredar los atributos de la clase Productos
    pass
    def __str__(self):
        ##la f es de format
        return f"CODIGO \t\t {self.codigo}\n"\
            f"NOMBRE \t\t {self.nombre}\n"\
            f"PRECIO \t\t {self.precio}\n"\
            f"DESCRIPCION \t {self.descripcion}\n"

class Alimentos(Productos):
    productor=''
    distribuidor=''
    ## quiero definir el __innit__
    # def __init__(self,codigo,nombre,precio,descripcion,productor,distribuidor):
    #     self.codigo=codigo
    #     self.nombre=nombre
    #     self.precio=precio
    #     self.descripcion=descripcion
    #     self.productor=productor
    #     self.distribuidor=distribuidor
    def __str__(self):
        ##la f es de format
        return f"CODIGO \t\t {self.codigo}\n"\
            f"NOMBRE \t\t {self.nombre}\n"\
            f"PRECIO \t\t {self.precio}\n"\
            f"DESCRIPCION \t {self.descripcion}\n"\
            f"PRODUCTOR \t {self.productor}\n"\
            f"DISTRIBUIDOR \t {self.distribuidor}\n"




adornos=Adornos(1,'lampara',120,'lampara de casa')
# print(adornos)
ali=Alimentos(1,'QUESO',1.20,'SIN SAL')
ali.productor='TU GRANJA'
ali.distribuidor='TU DISTIBUIDOR'
# print(ali)
lstProductos=[adornos,ali]

for p in lstProductos:
    
    if (isinstance(p,Adornos)):
        print(p.codigo,p.nombre)
    elif(isinstance(p,Alimentos)):
        print(p.codigo,p.nombre,p.distribuidor)
    
    
    
def descuento(Productos,rebaja):
    Productos.precio= Productos.precio-( Productos.precio/100*rebaja)

print(ali)
descuento(ali,50)
print(ali)