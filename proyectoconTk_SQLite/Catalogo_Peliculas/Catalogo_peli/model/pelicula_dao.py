from .conexion_db import ConexionDB
from tkinter  import messagebox

def crear_tabla():
    conexion=ConexionDB()
    sql='''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duración VARCHAR(10),
        genero varchar(100),
        primary key(id_pelicula autoincrement)
    ) '''
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        messagebox.showinfo(message='Se ha creado la tabla', title='CREATED')
    except:
        messagebox.showinfo(message='Ya existe una tabla', title='Error')
    

def eliminar_tabla():
    conexion=ConexionDB()

    sql='DROP TABLE peliculas'
    conexion.cursor.execute(sql)
    conexion.cerrar()

class pelicula:
    def __init__(self,nombre,duracion,genero):
        self.id_pelicula=None
        self.nombre=nombre
        self.duracion=duracion
        self.genero=genero
    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero}]'

def guardar(pelicula):
    conexion=ConexionDB()
    sql=f"""INSERT INTO peliculas(nombre,duración,genero)
    VALUES('{pelicula.nombre}','{pelicula.duracion}','{pelicula.genero}')"""
    
    
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except(Exception):
        
        titulo='CONEX al Registro'
        mensaje='Tabla no creada'
        messagebox.showerror(titulo,mensaje)

def listar():
    conexion=ConexionDB()
    lista_peliculas=[]
    sql='SELECT*FROM peliculas'

    try:
        conexion.cursor.execute(sql)
        lista_peliculas=conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        messagebox.showwarning('conexion al registro','no existe tabla')
    return lista_peliculas

def editar(pelicula,id_pelicula):
    conexion=ConexionDB()
    sql=f"""UPDATE peliculas
    SET nombre='{pelicula.nombre}',duración='{pelicula.duracion}',genero='{pelicula.genero}'
    where id_pelicula={id_pelicula}"""
    
   
    conexion.cursor.execute(sql)
    conexion.cerrar()
    
    
