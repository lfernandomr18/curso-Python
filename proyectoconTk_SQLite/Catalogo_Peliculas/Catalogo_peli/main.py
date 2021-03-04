import tkinter as tk
from client.gui_app import Frame,barra_menu

def main():
    ##creando GUI
    root=tk.Tk()
    root.title('Catalogo de Peliculas')
    root.iconbitmap('img\cp-logo.ico')
    root.resizable(0,0)
    ##llama a la barra de menu
    barra_menu(root)


    ##creado el Frame donde va todo dentro del a GUI
    app=Frame(root=root)

    
    ##hace que se mantenga abierto
    app.mainloop()

if __name__=='__main__':
    main()