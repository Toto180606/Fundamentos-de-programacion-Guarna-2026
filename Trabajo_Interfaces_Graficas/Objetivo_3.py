import tkinter as tk

def crear_ventana_login():
    
    ventana = tk.Tk()
    ventana.title("Login")
    ventana.geometry("300x130")
    ventana.resizable(0, 0)
    ventana.iconbitmap("c:/Users/totoy/Desktop/aplicaciones/visual/python/IMG_Grupo_19.ico")
    ventana.config(bg="#6d6969")

    lbl_usuario = tk.Label(ventana, text="Usuario Alumno: ", bg="#6d6969", fg="white")
    lbl_usuario.grid(row=0, column=0, padx=10, pady=10, sticky="w")

    ent_usuario = tk.Entry(ventana)
    ent_usuario.grid(row=0, column=1, padx=10)

    lbl_clave = tk.Label(ventana, text="Clave: ", bg="#6d6969", fg="white")
    lbl_clave.grid(row=1, column=0, padx=10, pady=10, sticky="w")

    ent_clave = tk.Entry(ventana, show="*")
    ent_clave.grid(row=1, column=1, padx=10)
    
    btn_ingresar = tk.Button(ventana, text="Ingresar")
    btn_ingresar.grid (row=2, column=0, columnspan=2, pady=15)

    ventana.mainloop()
    
crear_ventana_login()
