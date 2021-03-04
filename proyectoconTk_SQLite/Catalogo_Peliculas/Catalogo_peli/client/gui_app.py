import tkinter as tk
from tkinter import ttk

from model.pelicula_dao import crear_tabla,eliminar_tabla

def barra_menu(root):
    ##crea barra de menu
    barra_menu=tk.Menu(root)
    root.config(menu=barra_menu,width=300,height=300)
    ##crea la cascada INICIO,, el tearoff es para eliminar las
    menu_inicio=tk.Menu(barra_menu,tearoff=0)
    barra_menu.add_cascade(label='Inicio',menu=menu_inicio)

    barra_menu.add_cascade(label='Consultas')
    barra_menu.add_cascade(label='Configuración')
    barra_menu.add_cascade(label='Ayuda')
    ##añade subcascadas(command)
    menu_inicio.add_command(label='Crear Registro en DB',command=crear_tabla)
    menu_inicio.add_command(label='Eliminar Registro en DB',command=eliminar_tabla)
    menu_inicio.add_command(label='Salir',command=root.destroy)

class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.root=root
        self.pack()
        self.config(width=480,height=320)
        self.campos_pelicula()
        self.desabilitar_campos()
        self.tabla_peliculas()
        
    def campos_pelicula(self):

        ##Label de cada campo
        self.label_nombre=tk.Label(self,text='Nombre: ')
        self.label_nombre.config(font=('Arial',12,'bold'))
        self.label_nombre.grid(row=0,column=0,padx=10,pady=10)

        self.label_Duracion=tk.Label(self,text='Duración: ')
        self.label_Duracion.config(font=('Arial',12,'bold'))
        self.label_Duracion.grid(row=1,column=0,padx=10,pady=10)

        self.label_genero=tk.Label(self,text='Genero: ')
        self.label_genero.config(font=('Arial',12,'bold'))
        self.label_genero.grid(row=2,column=0,padx=10,pady=10)
        ##TextBox
        self.nombre=tk.StringVar()
        self.txt_nombre=tk.Entry(self,textvariable=self.nombre)
        self.txt_nombre.config(width=50,font=('Arial',12))
        self.txt_nombre.grid(row=0,column=1,padx=10,pady=10,columnspan=2)
        
        self.duracion=tk.StringVar()
        self.txt_Duracion=tk.Entry(self,textvariable=self.duracion)
        self.txt_Duracion.config(width=50,font=('Arial',12))
        self.txt_Duracion.grid(row=1,column=1,padx=10,pady=10,columnspan=2)

        self.genero=tk.StringVar()
        self.txt_Genero=tk.Entry(self,textvariable=self.genero)
        self.txt_Genero.config(width=50,font=('Arial',12))
        self.txt_Genero.grid(row=2,column=1,padx=10,pady=10,columnspan=2)

        ##Botones
        self.btn_nuevo=tk.Button(self,text='NUEVO',command=self.habilitar_campos)
        self.btn_nuevo.config(width=20,font=('Arial',12,'bold'),fg='white',bg='blue')
        self.btn_nuevo.grid(row=3,column=0,padx=10,pady=10)

        self.btn_Guardar=tk.Button(self,text='GUARDAR',command=self.guardar_datos)
        self.btn_Guardar.config(width=20,font=('Arial',12,'bold'),fg='white',bg='green')
        self.btn_Guardar.grid(row=3,column=1,padx=10,pady=10)

        self.btn_Cancelar=tk.Button(self,text='CANCELAR',command=self.desabilitar_campos)
        self.btn_Cancelar.config(width=20,font=('Arial',12,'bold'),fg='white',bg='red')
        self.btn_Cancelar.grid(row=3,column=2,padx=10,pady=10)

        self.btn_editar=tk.Button(self,text='EDITAR')
        self.btn_editar.config(width=20,font=('Arial',12,'bold'),fg='white',bg='blue')
        self.btn_editar.grid(row=5,column=0,padx=10,pady=10)

        self.btn_Eliminar=tk.Button(self,text='ELIMINAR')
        self.btn_Eliminar.config(width=20,font=('Arial',12,'bold'),fg='white',bg='red')
        self.btn_Eliminar.grid(row=5,column=1,padx=10,pady=10)

    def habilitar_campos(self):
        self.txt_nombre.config(state='normal')
        self.txt_Duracion.config(state='normal')
        self.txt_Genero.config(state='normal')

        self.btn_Guardar.config(state='normal')
        self.btn_Cancelar.config(state='normal')

    def desabilitar_campos(self):
        self.nombre.set('')
        self.duracion.set('')
        self.genero.set('')
        self.txt_nombre.config(state='disabled')
        self.txt_Duracion.config(state='disabled')
        self.txt_Genero.config(state='disabled')

        self.btn_Guardar.config(state='disabled')
        self.btn_Cancelar.config(state='disabled')
    
    def guardar_datos(self):
        self.desabilitar_campos()
    
    def tabla_peliculas(self):
        self.tabla=ttk.Treeview(self,column=('Nombre','Duración','Genero'))
        self.tabla.grid(row=4,column=0,columnspan=4)
        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Duración')
        self.tabla.heading('#3',text='Genero')
        self.tabla.insert('',0,text='1',values=('El señor de los anillos',2.30,'Fantasía'))




