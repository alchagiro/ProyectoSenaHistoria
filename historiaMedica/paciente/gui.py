from calendar import LocaleHTMLCalendar
from os import P_DETACH
import tkinter as tk
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel, LabelFrame
from tkinter import messagebox
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from modelo.historiaMedicaDao import historiaMedica, guardarHistoria, listarHistoria, eliminarHistoria, editarHistoria
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import Calendar
from datetime import datetime, date
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from auditoria import registrar_auditoria


class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#D3D6D3') #CDD8FF
        self.idPersona = None
        self.idPersonaHistoria = None
        self.idHistoriaMedica = None
        self.idHistoriaMedicaEditar = None
        self.camposPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def camposPaciente(self):

        #LABELS
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblNombre.grid(column=0, row=0, padx=10, pady=5)

        self.lblApePaterno = tk.Label(self, text='Apellido Paterno: ')
        self.lblApePaterno.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblApePaterno.grid(column=0,row=1, padx=10, pady=5)

        self.lblApeMaterno = tk.Label(self, text='Apellido Materno: ')
        self.lblApeMaterno.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblApeMaterno.grid(column=0,row=2, padx=10, pady=5)

        self.lblDni = tk.Label(self, text='Cedula: ')
        self.lblDni.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblDni.grid(column=0,row=3, padx=10, pady=5)

        self.lblFechNacimiento = tk.Label(self, text='Fecha Nacimiento: ')
        self.lblFechNacimiento.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblFechNacimiento.grid(column=0,row=4, padx=10, pady=5)

        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblEdad.grid(column=0,row=5, padx=10, pady=5)

        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblAntecedentes.grid(column=0,row=6, padx=10, pady=5)

        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblCorreo.grid(column=0,row=7, padx=10, pady=5)

        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblTelefono.grid(column=0,row=8, padx=10, pady=5)   

        #ENTRYS
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self, textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)

        self.svApePaterno = tk.StringVar()
        self.entryApePaterno = tk.Entry(self, textvariable=self.svApePaterno)
        self.entryApePaterno.config(width=50, font=('ARIAL',15))
        self.entryApePaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)

        self.svApeMaterno = tk.StringVar()
        self.entryApeMaterno = tk.Entry(self, textvariable=self.svApeMaterno)
        self.entryApeMaterno.config(width=50, font=('ARIAL',15))
        self.entryApeMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)

        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self, textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL',15))
        self.entryDni.grid(column=1, row=3, padx=10, pady=5, columnspan=2)

        self.svFecNacimiento = tk.StringVar()
        self.entryFecNacimiento = tk.Entry(self, textvariable=self.svFecNacimiento)
        self.entryFecNacimiento.config(width=50, font=('ARIAL',15))
        self.entryFecNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)

        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)

        self.svAntecentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self, textvariable=self.svAntecentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)

        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self, textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL',15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)

        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self, textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL',15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)

        #BUTTONS
        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#158645', cursor='hand2',activebackground='#35BD6F')
        self.btnNuevo.grid(column=0,row=9, padx=10, pady=5)

        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#007C79', cursor='hand2',activebackground='#99F2F0')
        self.btnGuardar.grid(column=1,row=9, padx=10, pady=5)

        self.btnCancelar = tk.Button(self, text='Cancelar',command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#007C79', cursor='hand2',activebackground='#99F2F0')
        self.btnCancelar.grid(column=2,row=9, padx=10, pady=5)

        #BUSCADOR
        #LABEL BUSCADOR
        self.lblBuscarDni = tk.Label(self, text='Buscar Cedula: ')
        self.lblBuscarDni.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblBuscarDni.grid(column=3, row=0, padx=10, pady=5)

        self.lblBuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblBuscarApellido.config(font=('ARIAl',15,'bold'), bg='#D3D6D3')
        self.lblBuscarApellido.grid(column=3, row=1, padx=10, pady=5)

        #ENTRYS BUSCADOR
        self.svBuscarDni = tk.StringVar()
        self.entryBuscarDni = tk.Entry(self, textvariable=self.svBuscarDni)
        self.entryBuscarDni.config(width=20, font=('ARIAL',15))
        self.entryBuscarDni.grid(column=4, row=0, padx=10, pady=5, columnspan=2)

        self.svBuscarApellido = tk.StringVar()
        self.entryBuscarApellido = tk.Entry(self, textvariable=self.svBuscarApellido)
        self.entryBuscarApellido.config(width=20, font=('ARIAL',15))
        self.entryBuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        #BUTTON BUSCADOR
        self.btnBuscarCondicion = tk.Button(self, text='Buscar', command = self.buscarCondicion)
        self.btnBuscarCondicion.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#007C79', cursor='hand2',activebackground='#99F2F0')
        self.btnBuscarCondicion.grid(column=3,row=2, padx=10, pady=5, columnspan=1)

        self.btnLimpiarBuscador = tk.Button(self, text='Limpiar', command = self.limpiarBuscador)
        self.btnLimpiarBuscador.config(width=20, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#007C79', cursor='hand2',activebackground='#99F2F0')
        self.btnLimpiarBuscador.grid(column=4,row=2, padx=10, pady=5, columnspan=1)

        #BUTTON CALENDARIO
        self.btnCalendario = tk.Button(self, text='Calendario', command = self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12,'bold'), fg='#DAD5D6', 
                                bg='#007C79', cursor='hand2',activebackground='#99F2F0')
        self.btnCalendario.grid(column=3,row=4, padx=10, pady=5, columnspan=1)

    def vistaCalendario(self):
        self.topCalendario = Toplevel()
        self.topCalendario.title("FECHA NACIMIENTO")
        self.topCalendario.resizable(0,0)
        self.topCalendario.iconbitmap('img/clinica.ico')
        self.topCalendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar(value='01-01-1990')
        self.calendar = tc.Calendar(self.topCalendario, selectmode='day', year=1990, month=1, day=1, locale ='es_US', bg='#777777', fg='#FFFFFF', headersbackground='#B6DDFE', textvariable=self.svCalendario, cursor = 'hand2', date_pattern='dd-mm-Y')
        self.calendar.pack(pady=22)
        self.calendar.grid(row=1, column = 0)

        #TRACE ENVIAR FECHA
        self.svCalendario.trace('w',self.enviarFecha)

    def enviarFecha(self, *args):
        # Se actualiza la fecha de nacimiento
        self.svFecNacimiento.set(self.svCalendario.get())
        # Se verifica si se ha seleccionado una fecha válida
        if self.svCalendario.get():
            # Se llama a la función para calcular la edad
            self.calcularEdad()


    def calcularEdad(self, *args):
        self.fechaActual = date.today()
        self.date1 = self.calendar.get_date()
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y")

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month, self.conver.day))
        self.svEdad.set(self.resul)

    def limpiarBuscador(self):
        self.svBuscarApellido.set('')
        self.svBuscarDni.set('')
        self.tablaPaciente()

    def buscarCondicion(self):
        if len(self.svBuscarDni.get()) > 0 or len(self.svBuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svBuscarDni.get())) > 0:
                where = "WHERE dni = " + self.svBuscarDni.get() + "" #WHERE dni = 87878787
            if (len(self.svBuscarApellido.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svBuscarApellido.get()+"%' AND activo = 1"
            
            self.tablaPaciente(where)
        else:
            self.tablaPaciente()

    def guardarPaciente(self):
        persona = Persona(
            self.svNombre.get(), self.svApePaterno.get(), self.svApeMaterno.get(),
            self.svDni.get(), self.svFecNacimiento.get(), self.svEdad.get(), self.svAntecentes.get(),
            self.svCorreo.get(), self.svTelefono.get()
        )

        if self.idPersona == None:
            guardarDatoPaciente(persona)
        else:
            editarDatoPaciente(persona, self.idPersona)

        

        
        self.deshabilitar()
        self.tablaPaciente()
        self.topCalendario.destroy()

    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='normal')
        self.entryApePaterno.config(state='normal')
        self.entryApeMaterno.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFecNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')

        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')

    def deshabilitar(self):
        self.idPersona = None
        self.svNombre.set('')
        self.svApePaterno.set('')
        self.svApeMaterno.set('')
        self.svDni.set('')
        self.svFecNacimiento.set('')
        self.svEdad.set('')
        self.svAntecentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='disabled')
        self.entryApePaterno.config(state='disabled')
        self.entryApeMaterno.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFecNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')

        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()
            #self.listaPersona.reverse()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'APaterno', 'AMaterno','Dni','FNacimiento','Edad','Antecedentes','Correo','Telefono'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky='nse')
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        self.tabla.heading('#0',text='ID')
        self.tabla.heading('#1',text='Nombre')
        self.tabla.heading('#2',text='Ap. Paterno')
        self.tabla.heading('#3',text='Ap. Materno')
        self.tabla.heading('#4',text='Dni')
        self.tabla.heading('#5',text='F. Nacimiento')
        self.tabla.heading('#6',text='Edad')
        self.tabla.heading('#7',text='Antecedentes')
        self.tabla.heading('#8',text='Correo')
        self.tabla.heading('#9',text='Telefono')

        self.tabla.column("#0", anchor=W, width=50)
        self.tabla.column("#1", anchor=W, width=150)
        self.tabla.column("#2", anchor=W, width=120)
        self.tabla.column("#3", anchor=W, width=120)
        self.tabla.column("#4", anchor=W, width=80)
        self.tabla.column("#5", anchor=W, width=100)
        self.tabla.column("#6", anchor=W, width=50)
        self.tabla.column("#7", anchor=W, width=300)
        self.tabla.column("#8", anchor=W, width=250)
        self.tabla.column("#9", anchor=W, width=82)

        for p in self.listaPersona:
            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]), tags=('evenrow',))

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command = self.eliminarDatoPaciente )
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#8A0000', activebackground='#D58A8A', cursor='hand2')
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnHistorialPaciente = tk.Button(self, text='Historial Paciente', command=self.historiaMedica)
        self.btnHistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnHistorialPaciente.grid(row=11, column=2, padx=10, pady=5)

        self.btnSalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnSalir.config(width=20,font=('ARIAL',12,'bold'), fg='#DAD5D6', bg='#007C79', activebackground='#99F2F0', cursor='hand2')
        self.btnSalir.grid(row=11, column=4, padx=10, pady=5)
 
    def exportar_pdf(self):
        try:
            # Obtener los datos seleccionados en la tabla de historias médicas
            seleccion = self.tablaHistoria.selection()
            if seleccion:
                # Obtener los datos de la fila seleccionada
                item = self.tablaHistoria.item(seleccion[0])
                datos = item['values']

                # Imprimir los datos para verificar
                print("Datos a exportar a PDF:", datos)

                # Crear un nuevo archivo PDF
                pdf_filename = "historiasPdf/historia_medica_{}.pdf".format(datos[0])  # Usar la fecha como nombre del archivo
                c = canvas.Canvas(pdf_filename, pagesize=letter)

                logo_path = "img/clinica.ico"    #INGRESO DEL BANER PARA EL DOCUMENTO O HISTORIA A IMPRIMIR 
                c.drawImage(logo_path, x=50, y=650)

                detalle = "Detalle: {}".format(datos[5])

                # Escribir los datos en el PDF
                c.drawString(50, 630, "Fecha y Hora: {}".format(datos[1]))
                c.drawString(50, 610, "Motivo: {}".format(datos[2]))
                c.drawString(50, 590, "Examen Auxiliar: {}".format(datos[3]))
                c.drawString(50, 570, "Tratamiento: {}".format(datos[4]))
                c.drawString(50, 550, "Detalle: {}".format(datos[5]))

                # Guardar y cerrar el PDF
                c.save()

                self.idHistoriaMedica = None
                self.topHistoriaMedica.destroy()

                messagebox.showinfo("Exportar a PDF", "Historia médica exportada a PDF correctamente.")
            else:
                messagebox.showwarning("Exportar a PDF", "Por favor, seleccione una historia médica para exportar.")
        except Exception as e:
            print(e)
            messagebox.showerror("Error", "Error al exportar la historia médica a PDF: {}".format(str(e)))


    def exportar_txt(self):   #AUN FALTA POR ESCRIBIR EN EL ARCHIVO
        try:
            # Obtener los datos seleccionados en la tabla de historias médicas
            seleccion = self.tablaHistoria.selection()
            if seleccion:
                # Obtener los datos de la fila seleccionada
                item = self.tablaHistoria.item(seleccion[0])
                datos = item['values']

                print("Datos a exportar a PDF:", datos)

                # Crear un nuevo archivo de texto
                txt_filename = "historiasPdf/historia_medica_{}.docx".format(datos[0])  # Usar la fecha como nombre del archivo
                with open(txt_filename, 'w') as file:
                    file.write("")
                    file.write("Fecha y Hora: {}\n".format(datos[1]))
                    file.write("Motivo: {}\n".format(datos[2]))
                    file.write("Examen Auxiliar: {}\n".format(datos[3]))
                    file.write("Tratamiento: {}\n".format(datos[4]))
                    file.write("Detalle: {}\n".format(datos[5]))

                messagebox.showinfo("Exportar a TXT", "Historia médica exportada a TXT correctamente.")
            else:
                messagebox.showwarning("Exportar a TXT", "Por favor, seleccione una historia médica para exportar.")
        except Exception as e:
            messagebox.showerror("Error", "Error al exportar la historia médica a TXT: {}".format(str(e)))




    def historiaMedica(self):

        try:
            if self.idPersona == None:
                self.idPersona = self.tabla.item(self.tabla.selection())['text']
                self.idPersonaHistoria = self.tabla.item(self.tabla.selection())['text']
            if (self.idPersona > 0):
                idPersona = self.idPersona
            
            self.topHistoriaMedica = Toplevel()
            self.topHistoriaMedica.title('HISTORIAL MEDICO')
            self.topHistoriaMedica.resizable(0,0)
            self.topHistoriaMedica.iconbitmap('img/clinica.ico')
            self.topHistoriaMedica.config(bg='#D3D6D3')

            self.listaHistoria = listarHistoria(idPersona)
            self.tablaHistoria = ttk.Treeview(self.topHistoriaMedica, column=('Apellidos','Fecha Historia', 'Motivo', 'Examen Auxiliar','Tratamiento', 'Detalle'))
            self.tablaHistoria.grid(row=0, column=0, columnspan=7, sticky='nse')

            self.scrollHistoria = ttk.Scrollbar(self.topHistoriaMedica, orient='vertical', command=self.tablaHistoria.yview)
            self.scrollHistoria.grid(row=0, column=8, sticky='nse')
            
            self.tablaHistoria.configure(yscrollcommand=self.scrollHistoria.set)

            self.tablaHistoria.heading('#0', text='ID')
            self.tablaHistoria.heading('#1', text='Nombre y Apellidos')
            self.tablaHistoria.heading('#2', text='Fecha y Hora')
            self.tablaHistoria.heading('#3', text='Motivo')
            self.tablaHistoria.heading('#4', text='Examen Auxiliar')
            self.tablaHistoria.heading('#5', text='Tratamiento')
            self.tablaHistoria.heading('#6', text='Detalle')

            self.tablaHistoria.column('#0', anchor=W, width=50)
            self.tablaHistoria.column('#1', anchor=W, width=150)
            self.tablaHistoria.column('#2', anchor=W, width=100)
            self.tablaHistoria.column('#3', anchor=W, width=120)
            self.tablaHistoria.column('#4', anchor=W, width=250)
            self.tablaHistoria.column('#5', anchor=W, width=200)
            self.tablaHistoria.column('#6', anchor=W, width=450)

            for p in self.listaHistoria:
                self.tablaHistoria.insert('',0, text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6]))

            self.btnGuardarHistoria = tk.Button(self.topHistoriaMedica, text='Agregar Historia', command=self.topAgregarHistoria)
            self.btnGuardarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
            self.btnGuardarHistoria.grid(row=2, column=0, padx=10, pady=5)

            self.btnEditarHistoria = tk.Button(self.topHistoriaMedica, text='Editar Historia', command=self.topEditarHistorialMedico)
            self.btnEditarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
            self.btnEditarHistoria.grid(row=2, column=1, padx=10, pady=5)

            self.btnEliminarHistoria = tk.Button(self.topHistoriaMedica, text='Eliminar Historia', command=self.eliminarHistorialMedico)
            self.btnEliminarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#890011', cursor='hand2', activebackground='#DB939C', state='disabled')
            self.btnEliminarHistoria.grid(row=2, column=2, padx=10, pady=5)

            self.btnExportarPDF = tk.Button(self.topHistoriaMedica, text='Exportar a PDF', command=self.exportar_txt)
            self.btnExportarPDF.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
            self.btnExportarPDF.grid(row=2, column=4, padx=10, pady=5)


            self.btnSalirHistoria = tk.Button(self.topHistoriaMedica, text='Salir', command=self.salirTop)
            self.btnSalirHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
            self.btnSalirHistoria.grid(row=2, column=6, padx=10, pady=5)


            self.idPersona = None
            
        except:
            title = 'Historia Medica'
            mensaje = 'Error al mostrar historial'
            messagebox.showerror(title, mensaje)
            self.idPersona = None

    def topAgregarHistoria(self):
        self.topAHistoria = Toplevel()
        self.topAHistoria.title('AGREGAR HISTORIA')
        self.topAHistoria.resizable(0,0)
        self.topAHistoria.iconbitmap('img/clinica.ico')
        self.topAHistoria.config(bg='#D3D6D3')
        #FRAME 1
        self.frameDatosHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameDatosHistoria.config(bg='#D3D6D3')
        self.frameDatosHistoria.pack(fill="both", expand="yes", pady=10, padx=20)

        #LABELS AGREGAR HISTORIA MEDICA
        self.lblMotivoHistoria = tk.Label(self.frameDatosHistoria, text='Motivo de la Historia Medica', width=30, font=('ARIAL', 15,'bold'), bg='#D3D6D3')
        self.lblMotivoHistoria.grid(row=0, column=0, padx=5, pady=3)

        self.lblExamenAuxiliarHistoria = tk.Label(self.frameDatosHistoria, text='Examen Auxiliar', width=20, font=('ARIAL', 15,'bold'), bg='#D3D6D3')
        self.lblExamenAuxiliarHistoria.grid(row=2, column=0, padx=5, pady=3)
        
        self.lblTratamientoHistoria = tk.Label(self.frameDatosHistoria, text='Tratamiento', width=20, font=('ARIAL', 15,'bold'), bg='#D3D6D3')
        self.lblTratamientoHistoria.grid(row=4, column=0, padx=5, pady=3)

        self.lblDetalleHistoria = tk.Label(self.frameDatosHistoria, text='Detalle de la Historia Medica', width=30, font=('ARIAL', 15,'bold'), bg='#D3D6D3')
        self.lblDetalleHistoria.grid(row=6, column=0, padx=5, pady=3)

        #ENTRYS AGREGA HISTORIA MEDICA
        self.svMotivoHistoria = tk.StringVar()
        self.motivoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svMotivoHistoria)
        self.motivoHistoria.config(width=64, font=('ARIAL', 15))
        self.motivoHistoria.grid(row=1, column=0, padx= 5, pady=3, columnspan=2)

        self.svExamenAuxiliarHistoria = tk.StringVar()
        self.examenAuxiliarHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svExamenAuxiliarHistoria)
        self.examenAuxiliarHistoria.config(width=64, font=('ARIAL', 15))
        self.examenAuxiliarHistoria.grid(row=3, column=0, padx= 5, pady=3, columnspan=2)

        self.svTratamientoHistoria = tk.StringVar()
        self.tratamientoHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svTratamientoHistoria)
        self.tratamientoHistoria.config(width=64, font=('ARIAL', 15))
        self.tratamientoHistoria.grid(row=5, column=0, padx= 5, pady=3, columnspan=2)

        self.svDetalleHistoria = tk.StringVar()
        self.detalleHistoria = tk.Entry(self.frameDatosHistoria, textvariable=self.svDetalleHistoria)
        self.detalleHistoria.config(width=64, font=('ARIAL', 15))
        self.detalleHistoria.grid(row=7, column=0, padx= 5, pady=3, columnspan=2)
        #FRAME 2
        self.frameFechaHistoria = tk.LabelFrame(self.topAHistoria)
        self.frameFechaHistoria.config(bg='#D3D6D3')
        self.frameFechaHistoria.pack(fill="both", expand="yes", padx=20,pady=10)

        #LABEL FECHA AGREGAR HISTORIA
        self.lblFechaHistoria = tk.Label(self.frameFechaHistoria, text='Fecha y Hora', width=20, font=('ARIAL', 15, 'bold'), bg='#D3D6D3')
        self.lblFechaHistoria.grid(row=1, column=0, padx=5, pady=3)
        
        #ENTRY FECHA AGREGAR HISTORIA
        self.svFechaHistoria = tk.StringVar()
        self.entryFechaHistoria = tk.Entry(self.frameFechaHistoria, textvariable=self.svFechaHistoria)
        self.entryFechaHistoria.config(width=20, font=('ARIAL', 15))
        self.entryFechaHistoria.grid(row=1, column=1, padx=5, pady=3)
        #TRAER FECHA Y HORA ACTUAL
        self.svFechaHistoria.set(datetime.today().strftime('%d-%m-%Y %H:%M'))

        #BUTTONS AGREGA HISTORIA
        self.btnAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Agregar Historia', command=self.agregaHistorialMedico)
        self.btnAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
        self.btnAgregarHistoria.grid(row=2, column=0, padx=10, pady=5)

        self.btnSalirAgregarHistoria = tk.Button(self.frameFechaHistoria, text='Salir',command=self.topAHistoria.destroy)
        self.btnSalirAgregarHistoria.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
        self.btnSalirAgregarHistoria.grid(row=2, column=3, padx=10, pady=5)

        self.idPersona = None

    def agregaHistorialMedico(self):
        try:
            if self.idHistoriaMedica == None:
                guardarHistoria(self.idPersonaHistoria, self.svFechaHistoria.get(),self.svMotivoHistoria.get(), self.svExamenAuxiliarHistoria.get(), self.svTratamientoHistoria.get(),self.svDetalleHistoria.get())
            self.topAHistoria.destroy()
            self.topHistoriaMedica.destroy()
            self.idPersona = None
        except:
            title = 'Agregar Historia'
            mensaje = 'Error al agregar historia Medica'
            messagebox.showerror(title, mensaje)

    def eliminarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            eliminarHistoria(self.idHistoriaMedica)

            self.idHistoriaMedica = None
            self.topHistoriaMedica.destroy()
        except:
            title = 'Eliminar Historia'
            mensaje = 'Erro al eliminar'
            messagebox.showerror(title, mensaje)

    def topEditarHistorialMedico(self):
        try:
            self.idHistoriaMedica = self.tablaHistoria.item(self.tablaHistoria.selection())['text']
            self.fechaHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][1]
            self.motivoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][2]
            self.exaMenAuxliarHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][3]
            self.tratamientoHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][4]
            self.detalleHistoriaEditar = self.tablaHistoria.item(self.tablaHistoria.selection())['values'][5]

            self.topEditarHistoria = Toplevel()
            self.topEditarHistoria.title('EDITAR HISTORIA MEDICA')
            self.topEditarHistoria.resizable(0,0)
            self.topEditarHistoria.iconbitmap('img/clinica.ico')
            self.topEditarHistoria.config(bg='#D3D6D3')

            #FRAME EDITAR DATOS HISTORIA.
            self.frameEditarHistoria = tk.LabelFrame(self.topEditarHistoria)
            self.frameEditarHistoria.config(bg='#D3D6D3')
            self.frameEditarHistoria.pack(fill="both", expand="yes", padx=20,pady=10)

            #LABEL EDITAR HISTORIA
            self.lblMotivoEditar = tk.Label(self.frameEditarHistoria, text='Motivo de la historia', width=30, font=('ARIAL', 15, 'bold'), bg='#D3D6D3')
            self.lblMotivoEditar.grid(row=0, column=0, padx=5, pady=3)

            self.lblExamenAuxiliarEditar = tk.Label(self.frameEditarHistoria, text='Examen Auxiliar', width=30, font=('ARIAL', 15, 'bold'), bg='#D3D6D3')
            self.lblExamenAuxiliarEditar.grid(row=2, column=0, padx=5, pady=3)

            self.lblTratamientoEditar = tk.Label(self.frameEditarHistoria, text='Tratamiento', width=30, font=('ARIAL', 15, 'bold'), bg='#D3D6D3')
            self.lblTratamientoEditar.grid(row=4, column=0, padx=5, pady=3)

            self.lblDetalleEditar = tk.Label(self.frameEditarHistoria, text='Detalle de la historia', width=30, font=('ARIAL', 15, 'bold'), bg='#D3D6D3')
            self.lblDetalleEditar.grid(row=6, column=0, padx=5, pady=3)

            #ENTRYS EDITAR HISTORIA

            self.svMotivoEditar = tk.StringVar()
            self.entryMotivoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svMotivoEditar)
            self.entryMotivoEditar.config(width=65, font=('ARIAL', 15))
            self.entryMotivoEditar.grid(row = 1, column=0, pady=3, padx=5, columnspan=2)

            self.svExamenAuxiliarEditar = tk.StringVar()
            self.entryExamenAuxiliarEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svExamenAuxiliarEditar)
            self.entryExamenAuxiliarEditar.config(width=65, font=('ARIAL', 15))
            self.entryExamenAuxiliarEditar.grid(row = 3, column=0, pady=3, padx=5, columnspan=2)

            self.svTratamientoEditar = tk.StringVar()
            self.entryTratamientoEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svTratamientoEditar)
            self.entryTratamientoEditar.config(width=65, font=('ARIAL', 15))
            self.entryTratamientoEditar.grid(row = 5, column=0, pady=3, padx=5, columnspan=2)

            self.svDetalleEditar = tk.StringVar()
            self.entryDetalleEditar = tk.Entry(self.frameEditarHistoria, textvariable=self.svDetalleEditar)
            self.entryDetalleEditar.config(width=65, font=('ARIAL', 15))
            self.entryDetalleEditar.grid(row = 7, column=0, pady=3, padx=5, columnspan=2)

            #FRAME FECHA EDITAR
            self.frameFechaEditar = tk.LabelFrame(self.topEditarHistoria)
            self.frameFechaEditar.config(bg='#D3D6D3')
            self.frameFechaEditar.pack(fill="both", expand="yes", padx=20, pady=10)
            
            #LABEL FECHA EDITAR
            self.lblFechaHistoriaEditar = tk.Label(self.frameFechaEditar, text='Fecha y Hora', width=30, font=('ARIAL', 15, 'bold'), bg='#D3D6D3')
            self.lblFechaHistoriaEditar.grid(row=1, column=0, padx=5, pady=3)

            #  ENTRY FECHA EDITAR
            self.svFechaHistoriaEditar = tk.StringVar()
            self.entryFechaHistoriaEditar = tk.Entry(self.frameFechaEditar, textvariable=self.svFechaHistoriaEditar)
            self.entryFechaHistoriaEditar.config(width=20, font=('ARIAL', 15))
            self.entryFechaHistoriaEditar.grid(row = 1, column=1, pady=3, padx=5)

            #INSERTAR LOS VALORES A LOS ENTRYS
            self.entryMotivoEditar.insert(0, self.motivoHistoriaEditar)
            self.entryExamenAuxiliarEditar.insert(0, self.exaMenAuxliarHistoriaEditar)
            self.entryTratamientoEditar.insert(0, self.tratamientoHistoriaEditar)
            self.entryDetalleEditar.insert(0, self.detalleHistoriaEditar)
            self.entryFechaHistoriaEditar.insert(0, self.fechaHistoriaEditar)

            #BUTTON EDITAR HISTORIA
            self.btnEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Editar Historia', command = self.historiaMedicaEditar)
            self.btnEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
            self.btnEditarHistoriaMedica.grid(row=2, column=0, padx=10, pady=5)

            self.btnSalirEditarHistoriaMedica = tk.Button(self.frameFechaEditar, text='Salir', command=self.topEditarHistoria.destroy)
            self.btnSalirEditarHistoriaMedica.config(width=20, font=('ARIAL', 12, 'bold'), fg='#DAD5D6', bg='#007C79', cursor='hand2', activebackground='#99F2F0')
            self.btnSalirEditarHistoriaMedica.grid(row=2, column=1, padx=10, pady=5)

            
            if self.idHistoriaMedicaEditar == None:
                self.idHistoriaMedicaEditar = self.idHistoriaMedica

            self.idHistoriaMedica = None
        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)


    def historiaMedicaEditar(self):
        try:
            editarHistoria(self.svFechaHistoriaEditar.get(), self.svMotivoEditar.get(), self.svExamenAuxiliarEditar.get(), self.svTratamientoEditar.get(), self.svDetalleEditar.get(), self.idHistoriaMedicaEditar)
            self.idHistoriaMedicaEditar = None
            self.idHistoriaMedica = None
            self.topEditarHistoria.destroy()
            self.topHistoriaMedica.destroy()
        except:
            title = 'Editar Historia'
            mensaje = 'Error al editar historia'
            messagebox.showerror(title, mensaje)
            self.topEditarHistoria.destroy()

    def salirTop(self):
        self.topHistoriaMedica.destroy()
        self.topAHistoria.destroy()
        self.topEditarHistoria.destroy()
        self.idPersona = None

    def editarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text'] #Trae el ID
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente = self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApePaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryApeMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entryDni.insert(0, self.dniPaciente)
            self.entryFecNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0,self.edadPaciente)
            self.entryAntecedentes.insert(0,self.antecedentesPaciente)
            self.entryCorreo.insert(0,self.correoPaciente)
            self.entryTelefono.insert(0,self.telefonoPaciente)
        except:
            title = 'Editar Paciente'
            mensaje = 'Error al editar paciente'
            messagebox.showerror(title, mensaje)
    
    def eliminarDatoPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            
            self.tablaPaciente()
            self.idPersona = None
        except:
            title = 'Eliminar Paciente'
            mensaje = 'No se pudo eliminar paciente'
            messagebox.showinfo(title, mensaje)