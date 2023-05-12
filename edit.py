import tkinter as tk
from tkcalendar import DateEntry
from tkinter import messagebox
import json
from datetime import datetime
from trabajador import Trabajador
class Editar:
    
    def __init__(self, indice):
        self.indice = indice
        self.ventana = tk.Tk()
        self.ventana.title("Guardar trabajador")
        self.ventana.resizable(False,False)
        self.nombre_entry = None
        self.apellido1_entry = None
        self.apellido2_entry = None
        self.cargo_entry = None
        self.empresa_entry = None
        self.calle_entry = None
        self.numeroExt_entry = None
        self.numeroInt_entry = None
        self.colonia_entry = None
        self.municipio_entry = None
        self.estado_entry = None
        self.codigoPostal_entry = None
        self.telefono_entry = None
        self.correoElectronico_entry = None
        self.fechaNacimiento_entry = None
        self.guardar_button = None

    def crear_ventana(self):
        # Crear los campos para ingresar los datos del trabajador
        tk.Label(self.ventana, text="Nombre:").grid(row=0, column=0)
        self.nombre_entry = tk.Entry(self.ventana)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(self.ventana, text="Apellido paterno:").grid(row=1, column=0)
        self.apellido1_entry = tk.Entry(self.ventana)
        self.apellido1_entry.grid(row=1, column=1)

        tk.Label(self.ventana, text="Apellido materno:").grid(row=2, column=0)
        self.apellido2_entry = tk.Entry(self.ventana)
        self.apellido2_entry.grid(row=2, column=1)

        tk.Label(self.ventana, text="Cargo:").grid(row=3, column=0)
        self.cargo_entry = tk.Entry(self.ventana)
        self.cargo_entry.grid(row=3, column=1)

        tk.Label(self.ventana, text="Empresa:").grid(row=4, column=0)
        self.empresa_entry = tk.Entry(self.ventana)
        self.empresa_entry.grid(row=4, column=1)

        tk.Label(self.ventana, text="Calle:").grid(row=5, column=0)
        self.calle_entry = tk.Entry(self.ventana)
        self.calle_entry.grid(row=5, column=1)

        tk.Label(self.ventana, text="Número exterior:").grid(row=6, column=0)
        self.numeroExt_entry = tk.Entry(self.ventana)
        self.numeroExt_entry.grid(row=6, column=1)

        tk.Label(self.ventana, text="Número interior:").grid(row=7, column=0)
        self.numeroInt_entry = tk.Entry(self.ventana)
        self.numeroInt_entry.grid(row=7, column=1)

        tk.Label(self.ventana, text="Colonia:").grid(row=8, column=0)
        self.colonia_entry = tk.Entry(self.ventana)
        self.colonia_entry.grid(row=8, column=1)

        tk.Label(self.ventana, text="Municipio:").grid(row=9, column=0)
        self.municipio_entry = tk.Entry(self.ventana)
        self.municipio_entry.grid(row=9, column=1)

        tk.Label(self.ventana, text="Estado:").grid(row=10, column=0)
        self.estado_entry = tk.Entry(self.ventana)
        self.estado_entry.grid(row=10, column=1)

        tk.Label(self.ventana, text="Código postal:").grid(row=11, column=0)
        self.codigoPostal_entry = tk.Entry(self.ventana)
        self.codigoPostal_entry.grid(row=11, column=1)

        tk.Label(self.ventana, text="Teléfono:").grid(row=12, column=0)
        self.telefono_entry = tk.Entry(self.ventana)
        self.telefono_entry.grid(row=12, column=1)

        tk.Label(self.ventana, text="Correo electrónico:").grid(row=13, column=0)
        self.correoElectronico_entry = tk.Entry(self.ventana)
        self.correoElectronico_entry.grid(row=13, column=1)

        tk.Label(self.ventana, text="Fecha de nacimiento:").grid(row=14, column=0)
        self.fechaNacimiento_entry = DateEntry(self.ventana, date_pattern="yyyy-mm-dd", state="readonly")
        self.fechaNacimiento_entry.grid(row=14, column=1)

        # Crear el botón para guardar los datos del trabajador
        self.guardar_button = tk.Button(self.ventana, text="Guardar", command=self.guardar_trabajador)
        self.guardar_button.grid(row=15, column=1)

    def guardar_trabajador(self):
        # Obtener los datos del trabajador
        nombre = self.nombre_entry.get()
        apellido1 = self.apellido1_entry.get()
        apellido2 = self.apellido2_entry.get()
        cargo = self.cargo_entry.get()
        empresa = self.empresa_entry.get()
        calle = self.calle_entry.get()
        numeroExt = self.numeroExt_entry.get()
        numeroInt = self.numeroInt_entry.get()
        colonia = self.colonia_entry.get()
        municipio = self.municipio_entry.get()
        estado = self.estado_entry.get()
        codigoPostal = self.codigoPostal_entry.get()
        telefono = self.telefono_entry.get()
        correoElectronico = self.correoElectronico_entry.get()
        fechaNacimiento = self.fechaNacimiento_entry.get_date()

        # Guardar los datos del trabajador en una base de datos o archivo
        # ...

        if not numeroExt.isdigit():
            messagebox.showerror("Error", "El campo Número Ext. debe contener solo números")
            return

        if not numeroInt.isdigit():
            messagebox.showerror("Error", "El campo Número Int. debe contener solo números")
            return

        if not codigoPostal.isdigit():
            messagebox.showerror("Error", "El campo Código Postal debe contener solo números")
            return

        if not telefono.isdigit():
            messagebox.showerror("Error", "El campo Teléfono debe contener solo números")
            return

        trabajador = Trabajador(nombre, apellido1, apellido2, cargo, empresa, calle, numeroExt, numeroInt, colonia, municipio, estado, codigoPostal, telefono, correoElectronico, fechaNacimiento)
        data = []
        with open("db.json", "r") as f:
            data = json.load(f)

        # Creamos un diccionario con los datos del nuevo objeto
        nuevo_trabajador = {
            "nombre": trabajador.nombre,
            "apellido1": trabajador.apellido1,
            "apellido2": trabajador.apellido2,
            "cargo": trabajador.cargo,
            "empresa": trabajador.empresa,
            "calle": trabajador.calle,
            "numeroExt": trabajador.numeroExt,
            "numeroInt": trabajador.numeroInt,
            "colonia": trabajador.colonia,
            "municipio": trabajador.municipio,
            "estado": trabajador.estado,
            "codigoPostal": trabajador.codigoPostal,
            "telefono": trabajador.telefono,
            "correoElectronico": trabajador.correoElectronico,
            "fechaNacimiento": trabajador.fechaNacimiento.isoformat(),
            "edad": trabajador.edad
        }

        # Agregamos el diccionario del nuevo objeto a la lista de datos existentes
        data[self.indice] = nuevo_trabajador

        # Guardamos la lista actualizada en el archivo JSON
        with open("db.json", "w") as f:
            json.dump(data, f)
        
        messagebox.showinfo("Éxito", "¡El trabajador se ha editado con éxito!")
        self.ventana.destroy()

    def iniciar(self):
        self.crear_ventana()
        self.ventana.mainloop()

    def cargar_datos(self, indice):
        with open('db.json', 'r') as f:
            trabajadores = json.load(f)
        registro = trabajadores[self.indice]

    # Asignar los valores del registro a los campos correspondientes de la GUI
        self.nombre_entry.insert(0, registro['nombre'])
        self.apellido1_entry.insert(0, registro['apellido1'])
        self.apellido2_entry.insert(0, registro['apellido2'])
        self.cargo_entry.insert(0, registro['cargo'])
        self.empresa_entry.insert(0, registro['empresa'])
        self.calle_entry.insert(0, registro['calle'])
        self.numeroExt_entry.insert(0, registro['numeroExt'])
        self.numeroInt_entry.insert(0, registro['numeroInt'])
        self.colonia_entry.insert(0, registro['colonia'])
        self.municipio_entry.insert(0, registro['municipio'])
        self.estado_entry.insert(0, registro['estado'])
        self.codigoPostal_entry.insert(0, registro['codigoPostal'])
        self.telefono_entry.insert(0, registro['telefono'])
        self.correoElectronico_entry.insert(0, registro['correoElectronico'])
        
        fecha_de_nacimiento = registro['fechaNacimiento']
        birthdate = datetime.strptime(fecha_de_nacimiento, '%Y-%m-%d')
        self.fechaNacimiento_entry.set_date(birthdate)



# editar = Editar()
# editar.iniciar()