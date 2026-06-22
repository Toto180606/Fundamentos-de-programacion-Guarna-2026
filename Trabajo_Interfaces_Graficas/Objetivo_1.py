import tkinter as tk

def crear_ventana_login():
    
    ventana = tk.Tk()
    ventana.title("Login + Los Programadores del Feriado")
    ventana.geometry("300x130")
    ventana.resizable(0, 0)
    ventana.iconbitmap("c:/Users/totoy/Desktop/aplicaciones/visual/python/IMG_Grupo_19.ico")
    ventana.config(bg="#6d6969")
    ventana.mainloop()
    
crear_ventana_login()
