import sqlite3
from tkinter import messagebox


def registrar_auditoria(accion, usuario):
    try:
        conexion = sqlite3.connect('database/dbhistorial.db')
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO auditoria (accion, usuario) VALUES (?, ?)", (accion, usuario))
        conexion.commit()
        conexion.close()
    except Exception as e:
        messagebox.showerror("Error", "Error al registrar la auditoría: {}".format(str(e)))