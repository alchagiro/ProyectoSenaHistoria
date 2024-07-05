import tkinter as tk
from tkinter import simpledialog
from tkinter import messagebox
import sqlite3
from historiaMedica import main as abrir_historia_medica
from auditoria import registrar_auditoria


contraseña_maestra = "admin"

class LoginApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inicio de Sesión")
        
        # Variables para almacenar el nombre de usuario y la contraseña
        self.nombre_usuario = tk.StringVar()
        self.contraseña = tk.StringVar()
        
        # Etiquetas y campos de entrada
        tk.Label(root, text="Nombre de Usuario:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.nombre_usuario).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(root, text="Contraseña:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(root, textvariable=self.contraseña, show="*").grid(row=1, column=1, padx=5, pady=5)
        
        # Botón de inicio de sesión
        tk.Button(root, text="Iniciar Sesión", command=self.iniciar_sesion).grid(row=2, column=0, padx=5, pady=5)

        # Botón de registro de usuario
        tk.Button(root, text="Registrar Usuario", command=self.registrar_usuario).grid(row=2, column=1, columnspan=2, padx=5, pady=5)

        # Boton de Eliminar Usuario
        tk.Button(root, text="Eliminar Usuario", command=self.eliminar_usuario).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def iniciar_sesion(self):
        nombre_usuario = self.nombre_usuario.get()
        contraseña = self.contraseña.get()
        
        # Verificar las credenciales en la base de datos
        if self.verificar_credenciales(nombre_usuario, contraseña):
            messagebox.showinfo("Inicio de Sesión", "¡Inicio de sesión exitoso!")
            registrar_auditoria("Inicio Sesion", nombre_usuario)
            self.root.destroy()
            abrir_historia_medica()

        else:
            messagebox.showerror("Error de Inicio de Sesión", "Nombre de usuario o contraseña incorrectos.")

    def verificar_credenciales(self, nombre_usuario, contraseña):
        try:
            conexion = sqlite3.connect('database/dbhistorial.db')
            cursor = conexion.cursor()
            
            # Consultar la contraseña almacenada para el nombre de usuario proporcionado
            cursor.execute("SELECT password FROM usuarios WHERE username = ?", (nombre_usuario,))
            resultado = cursor.fetchone()
            
            if resultado:  # Si se encontró un usuario con ese nombre de usuario
                contraseña_almacenada = resultado[0]
                # Verificar si la contraseña proporcionada coincide con la almacenada
                if contraseña == contraseña_almacenada:
                    return True, nombre_usuario
                else:
                    return False, None
            else:
                return False  # Usuario no encontrado
            
            conexion.close()
        except Exception as e:
            messagebox.showerror("Error", "Error al verificar credenciales: {}".format(str(e)))

    def registrar_usuario(self):
        contraseña_confirmacion = simpledialog.askstring("Confirmar Contraseña", "Por favor, ingrese la contraseña maestra para registrar un nuevo usuario:", show="*")
        if contraseña_confirmacion is not None:
            if contraseña_confirmacion == contraseña_maestra:
                # Solicitar el nuevo nombre de usuario y contraseña
                nuevo_usuario = simpledialog.askstring("Registrar Usuario", "Ingrese el nuevo nombre de usuario:")
                nueva_contraseña = simpledialog.askstring("Registrar Usuario", "Ingrese la nueva contraseña:")
                
            # Verificar si se ingresaron el nombre de usuario y la contraseña
            if nuevo_usuario and nueva_contraseña:
                # Guardar el nuevo usuario en la base de datos
                self.guardar_usuario(nuevo_usuario, nueva_contraseña)
                messagebox.showinfo("Registro Exitoso", "Usuario registrado exitosamente.")
                registrar_auditoria("Registro de Usuario", nuevo_usuario)
            else:
                messagebox.showerror("Error", "Debe ingresar un nombre de usuario y una contraseña.")
            pass
        else:
            messagebox.showerror("Error", "La contraseña ingresada no es correcta.")


    def guardar_usuario(self, nombre_usuario, contraseña):
        try:
            conexion = sqlite3.connect('database/dbhistorial.db')
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (nombre_usuario, contraseña))
            conexion.commit()
            conexion.close()
        except Exception as e:
            messagebox.showerror("Error", "Error al registrar el usuario: {}".format(str(e)))

    def eliminar_usuario(self):
        # Solicitar la contraseña maestra para eliminar un usuario
        contraseña_confirmacion = simpledialog.askstring("Confirmar Contraseña", "Por favor, ingrese la contraseña maestra para eliminar un usuario:", show="*")
        if contraseña_confirmacion is not None:
            if contraseña_confirmacion == contraseña_maestra:
        # Solicitar confirmación antes de eliminar
                confirmacion = messagebox.askyesno("Confirmar Eliminación", "¿Está seguro de que desea eliminar su cuenta de usuario? Esto no se puede deshacer.")
                if confirmacion:
                    nombre_usuario = self.nombre_usuario.get()

                    try:
                        conexion = sqlite3.connect('database/dbhistorial.db')
                        cursor = conexion.cursor()

                        # Eliminar el usuario de la base de datos
                        cursor.execute("DELETE FROM usuarios WHERE username = ?", (nombre_usuario,))
                        conexion.commit()
                        conexion.close()

                        messagebox.showinfo("Usuario Eliminado", "Su cuenta de usuario ha sido eliminada exitosamente.")
                        registrar_auditoria("Usuario Eliminado", nombre_usuario)
                    except Exception as e:
                        messagebox.showerror("Error", "Error al eliminar usuario: {}".format(str(e)))
                pass
        else:
            messagebox.showerror("Error", "La contraseña ingresada no es correcta.")


# Crear la ventana principal de la aplicación
root = tk.Tk()
app = LoginApp(root)
root.resizable(0,0)
root.iconbitmap('img/clinica.ico')
root.mainloop()

