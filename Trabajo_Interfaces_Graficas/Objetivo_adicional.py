import tkinter as tk
import os
from tkinter import messagebox

usuarios_claves = {
    "Tomas": "clave1",
    "Lautaro": "clave2",
    "Brian": "clave3",
    "Abril": "clave4",
    "Agustina": "clave5",
    "Nicolas": "clave6"
}

def validar_login(usuario, clave):
    if usuario in usuarios_claves and usuarios_claves[usuario] == clave:
        messagebox.showinfo("Login", "Usuario y Clave Correctos")
    else:
        messagebox.showerror("Login", "Alguno de los datos ingresados es Incorrecto")

def abrir_ventana_registro(ventana):
    ventana_reg = tk.Toplevel(ventana)
    ventana_reg.transient(ventana)
    ventana_reg.grab_set()
    ventana_reg.title("Registro de Usuario")
    ventana_reg.resizable(0,0)
    ventana_reg.geometry("300x130") 
    ventana_reg.config(bg="#4a4a4a")
    
    ruta_icono = os.path.join(os.path.dirname(__file__), "IMG_Grupo_19.ico")
    try:
        ventana_reg.iconbitmap(ruta_icono)
    except Exception as e:
        print(e)
    
    
    marco_reg = tk.Frame(ventana_reg, bg="#4a4a4a", padx=15, pady=10)
    marco_reg.pack(fill=tk.BOTH, expand=True)
    
  
    lbl_nuevo_user = tk.Label(marco_reg, text="Nuevo Usuario:", bg="#4a4a4a", fg="white")
    lbl_nuevo_user.grid(row=0, column=0, padx=5, pady=5, sticky="w")
    
    ent_nuevo_user = tk.Entry(marco_reg, width=18)
    ent_nuevo_user.grid(row=0, column=1, padx=5, pady=5)
    
    lbl_nueva_pass = tk.Label(marco_reg, text="Nueva Clave:", bg="#4a4a4a", fg="white")
    lbl_nueva_pass.grid(row=1, column=0, padx=5, pady=5, sticky="w")
    
    ent_nueva_pass = tk.Entry(marco_reg, show="*", width=18)
    ent_nueva_pass.grid(row=1, column=1, padx=5, pady=5)
    
    def guardar_usuario():
        user = ent_nuevo_user.get().strip()
        pas = ent_nueva_pass.get().strip()
        if user == "" or pas == "":
            messagebox.showwarning("Atención", "Completá todos los campos")
        elif user in usuarios_claves:
            messagebox.showerror("Error", "El usuario ya existe")
        else:
            usuarios_claves[user] = pas
            messagebox.showinfo("Éxito", f"Usuario {user} registrado correctamente")
            ventana_reg.destroy() 

   
    btn_guardar = tk.Button(marco_reg, text="Guardar Registro", command=guardar_usuario)
    btn_guardar.grid(row=2, column=0, columnspan=2, pady=10)

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Login grupo 19")
    ventana.resizable(0,0)
    ventana.geometry("360x180") 
    ventana.configure(bg="#6d6969")
    
    ruta_icono = os.path.join(os.path.dirname(__file__), "IMG_Grupo_19.ico")
    try:
       
        ventana.iconbitmap(ruta_icono)
    except Exception as e:
        print(e)

    marco = tk.Frame(ventana, padx=20, pady=15, background="#6d6969")
    marco.pack(fill=tk.BOTH, expand=True)

    lbl_usuario_alumno = tk.Label(marco, text="Usuario alumno:", bg="#6d6969", fg="white")
    lbl_usuario_alumno.grid(row=0, column=0, padx=10, pady=5, sticky="w")

    entry_usuario_alumno = tk.Entry(marco)
    entry_usuario_alumno.grid(row=0, column=1, padx=10, pady=5, sticky="w")

    lbl_clave = tk.Label(marco, text="Clave:", bg="#6d6969", fg="white")
    lbl_clave.grid(row=1, column=0, padx=10, pady=5, sticky="w")

    entry_clave = tk.Entry(marco, show="*")
    entry_clave.grid(row=1, column=1, padx=10, pady=5, sticky="w")

    btn_registrar_user = tk.Button(marco, text="Registrarse", command=lambda: abrir_ventana_registro(ventana))
    btn_registrar_user.grid(row=2, column=0, padx=10, pady=20, sticky="w")

    btn_ingresar = tk.Button(marco, text="Ingresar", command=lambda: validar_login(entry_usuario_alumno.get(), entry_clave.get()))
    btn_ingresar.grid(row=2, column=1, padx=10, pady=20, sticky="e")

    ventana.mainloop()

if __name__ == "__main__":
    crear_ventana()
