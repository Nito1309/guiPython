import tkinter as tk
from tkinter import messagebox
from tkcalendar import DateEntry
import datetime
from trabajador import Trabajador
import json

def guardar():
    nombre = nombre_entry.get()
    apellido1 = apellido1_entry.get()
    apellido2 = apellido2_entry.get()
    cargo = cargo_entry.get()
    empresa = empresa_entry.get()
    calle = calle_entry.get()
    numeroExt = numeroExt_entry.get()
    numeroInt = numeroInt_entry.get()
    colonia = colonia_entry.get()
    municipio = municipio_entry.get()
    estado = estado_entry.get()
    codigoPostal = codigoPostal_entry.get()
    telefono = telefono_entry.get()
    correoElectronico = correoElectronico_entry.get()
    fechaNacimiento = fechaNacimiento_entry.get_date()

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
    data.append(nuevo_trabajador)

    # Guardamos la lista actualizada en el archivo JSON
    with open("db.json", "w") as f:
        json.dump(data, f)
    
    messagebox.showinfo("Éxito", "¡El trabajador ha sido guardado con éxito!")
    ventana.destroy()


# Crear la ventana principal

ventana = tk.Tk()
ventana.title("Guardar trabajador")
ventana.resizable(False,False)
# Crear los campos para ingresar los datos del trabajador
tk.Label(ventana, text="Nombre:").grid(row=0, column=0)
nombre_entry = tk.Entry(ventana)
nombre_entry.grid(row=0, column=1)

tk.Label(ventana, text="Apellido paterno:").grid(row=1, column=0)
apellido1_entry = tk.Entry(ventana)
apellido1_entry.grid(row=1, column=1)

tk.Label(ventana, text="Apellido materno:").grid(row=2, column=0)
apellido2_entry = tk.Entry(ventana)
apellido2_entry.grid(row=2, column=1)

tk.Label(ventana, text="Cargo:").grid(row=3, column=0)
cargo_entry = tk.Entry(ventana)
cargo_entry.grid(row=3, column=1)

tk.Label(ventana, text="Empresa:").grid(row=4, column=0)
empresa_entry = tk.Entry(ventana)
empresa_entry.grid(row=4, column=1)

tk.Label(ventana, text="Calle:").grid(row=5, column=0)
calle_entry = tk.Entry(ventana)
calle_entry.grid(row=5, column=1)

tk.Label(ventana, text="Número exterior:").grid(row=6, column=0)
numeroExt_entry = tk.Entry(ventana)
numeroExt_entry.grid(row=6, column=1)

tk.Label(ventana, text="Número interior:").grid(row=7, column=0)
numeroInt_entry = tk.Entry(ventana)
numeroInt_entry.grid(row=7, column=1)

tk.Label(ventana, text="Colonia:").grid(row=8, column=0)
colonia_entry = tk.Entry(ventana)
colonia_entry.grid(row=8, column=1)

tk.Label(ventana, text="Municipio:").grid(row=9, column=0)
municipio_entry = tk.Entry(ventana)
municipio_entry.grid(row=9, column=1)

tk.Label(ventana, text="Estado:").grid(row=10, column=0)
estado_entry = tk.Entry(ventana)
estado_entry.grid(row=10, column=1)

tk.Label(ventana, text="Código postal:").grid(row=11, column=0)
codigoPostal_entry = tk.Entry(ventana)
codigoPostal_entry.grid(row=11, column=1)

tk.Label(ventana, text="Teléfono:").grid(row=12, column=0)
telefono_entry = tk.Entry(ventana)
telefono_entry.grid(row=12, column=1)

tk.Label(ventana, text="Correo electrónico:").grid(row=13, column=0)
correoElectronico_entry = tk.Entry(ventana)
correoElectronico_entry.grid(row=13, column=1)

tk.Label(ventana, text="Fecha de nacimiento:").grid(row=14, column=0)
fechaNacimiento_entry = DateEntry(ventana, date_pattern="yyyy-mm-dd", state="readonly")
fechaNacimiento_entry.grid(row=14, column=1)

# Crear un botón para guardar el trabajador
guardar_button = tk.Button(ventana, text="Guardar", command=guardar)
guardar_button.grid(row=15, column=0, columnspan=2, pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
