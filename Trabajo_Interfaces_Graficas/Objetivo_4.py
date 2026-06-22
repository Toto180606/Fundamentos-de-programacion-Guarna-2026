import tkinter as tk
from tkinter import messagebox


def obtener_usuarios_claves():
    return {
        "Tomas": "clave1",
        "Lautaro": "clave2",
        "brian": "clave3",
        "Abril": "clave4",
        "Agustina": "clave5",
        "Nicolas": "clave6"
    }

def verificar_usuarios(usuario, password):
    usuarios = obtener_usuarios_claves()
 
    if usuario in usuarios and usuarios[usuario] == password:
        messagebox.showinfo("Éxito", "Usuario y Clave Correctos")
    else:
        messagebox.showerror("Error", "Algunos de los datos ingresados es Incorrecto")

def crear_ventana_login():
    ventana = tk.Tk()
    ventana.title("Login - Grupo 19")
    ventana.geometry("300x130") 
    ventana.resizable(0, 0)
    ventana.iconbitmap("c:/Users/totoy/Desktop/aplicaciones/visual/python/IMG_Grupo_19.ico")
    ventana.config(bg="#6d6969")

    tk.Label(ventana, text="Usuario Alumno: ", bg="#6d6969", fg="white").grid(row=0, column=0, padx=10, pady=10, sticky="w")
    ent_usuario = tk.Entry(ventana)
    ent_usuario.grid(row=0, column=1, padx=10)

    tk.Label(ventana, text="Clave: ", bg="#6d6969", fg="white").grid(row=1, column=0, padx=10, pady=10, sticky="w")
    ent_clave = tk.Entry(ventana, show="*")
    ent_clave.grid(row=1, column=1, padx=10)

    btn_ingresar = tk.Button(ventana, text="Ingresar", command=lambda: verificar_usuarios(ent_usuario.get(), ent_clave.get()))
    btn_ingresar.grid(row=2, column=0, columnspan=2, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana_login()
