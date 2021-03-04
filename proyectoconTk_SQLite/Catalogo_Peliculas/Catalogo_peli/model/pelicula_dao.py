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