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
    # quiero definir el __innit__
    def __init__(self,codigo,nombre,precio,descripcion,productor,distribuidor):
        Productos.__init__(self,codigo,nombre,precio,descripcion)
       
        self.productor=productor
        self.distribuidor=distribuidor
    def __str__(self):
        ##la f es de format
        return f"CODIGO \t\t {self.codigo}\n"\
            f"NOMBRE \t\t {self.nombre}\n"\
            f"PRECIO \t\t {self.precio}\n"\
            f"DESCRIPCION \t {self.descripcion}\n"\
            f"PRODUCTOR \t {self.productor}\n"\
            f"DISTRIBUIDOR \t {self.distribuidor}\n"


class Moto(Productos):
    def __init__(self,codigo,nombre,precio,descripcion,kilometraje):
        super().__init__(codigo,nombre,precio,descripcion)
        self.kilometraje=kilometraje

    def __str__(self):
        return f'Nombre: {self.nombre} \nKilometraje:  {self.kilometraje}'



# adornos=Adornos(1,'lampara',120,'lampara de casa')
# # print(adornos)
# ali=Alimentos(1,'QUESO',1.20,'SIN SAL','TU PRODUCTOR','TU DISTRIBUIDOR')

# # print(ali)
# lstProductos=[adornos,ali]

# for p in lstProductos:
    
#     if (isinstance(p,Adornos)):
#         print(p.codigo,p.nombre)
#     elif(isinstance(p,Alimentos)):
#         print(p.codigo,p.nombre,p.distribuidor)


motito=Moto(1,'moto',120,'moto verde',1512)
print(motito)  
    
    
# def descuento(Productos,rebaja):
#     Productos.precio= Productos.precio-( Productos.precio/100*rebaja)

# print(ali)
# descuento(ali,50)
# print(ali)