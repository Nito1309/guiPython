import os
from tkinter import *
import json
from trabajador import Trabajador
import docx
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas as cv

def editar(indice):
    from edit import Editar
    editor = Editar(indice)
    editor.crear_ventana()  # Crear campos de entrada
    editor.cargar_datos(indice)  # Cargar datos del trabajador en los campos de entrada

def generar_oficio(i):

    with open("db.json", "r") as f:
        data = json.load(f)
    trabajador = data[i]

    with open("./plantillas/plantilla_oficio.txt", "r") as archivo:
        plantilla_oficio = archivo.read()


    oficio = plantilla_oficio.format(
        nombre=trabajador["nombre"],
        apellido1=trabajador["apellido1"],
        apellido2=trabajador["apellido2"],
        cargo=trabajador["cargo"],
        empresa=trabajador["empresa"],
        calle=trabajador["calle"],
        numeroExt=trabajador["numeroExt"],
        numeroInt=trabajador["numeroInt"],
        colonia=trabajador["colonia"],
        municipio=trabajador["municipio"],
        estado=trabajador["estado"],
        codigoPostal=trabajador["codigoPostal"],
        telefono=trabajador["telefono"],
        correoElectronico=trabajador["correoElectronico"],
        fechaNacimiento=trabajador["fechaNacimiento"],
        edad=trabajador["edad"]
    )
        
    nombre_archivo = f"./oficios/oficio_{i+1}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(oficio)



def generar_oficios():
    with open("db.json", "r") as archivo:
        data = json.load(archivo)
    informacion = [Trabajador(**info) for info in data]

    with open("./plantillas/plantilla_oficio.txt", "r") as archivo:
        plantilla_oficio = archivo.read()

    for i, trabajador in enumerate(informacion):
        oficio = plantilla_oficio.format(
            nombre=trabajador.nombre,
            apellido1=trabajador.apellido1,
            apellido2=trabajador.apellido2,
            cargo=trabajador.cargo,
            empresa=trabajador.empresa,
            calle=trabajador.calle,
            numeroExt=trabajador.numeroExt,
            numeroInt=trabajador.numeroInt,
            colonia=trabajador.colonia,
            municipio=trabajador.municipio,
            estado=trabajador.estado,
            codigoPostal=trabajador.codigoPostal,
            telefono=trabajador.telefono,
            correoElectronico=trabajador.correoElectronico,
            fechaNacimiento=trabajador.fechaNacimiento,
            edad=trabajador.edad
        )
        
        nombre_archivo = f"./oficios/oficio_{i+1}.txt"
        with open(nombre_archivo, "w") as archivo:
            archivo.write(oficio)

    print("Oficios creados correctamente")


def borrar_trabajador(i):
    print(i)
    if not trabajadores.count(i) == 1:
    # Eliminar el trabajador correspondiente del archivo db.json
        with open("db.json", "r") as f:
            data = json.load(f)
        del data[i]
        with open("db.json", "w") as f:
            json.dump(data, f)

        subframe = frame.grid_slaves(row=i+1)[0]
        subframe.destroy()

        # Actualizar los subframes restantes
        for j in range(i+1, len(trabajadores)+1):
            subframe = frame.grid_slaves(row=j+1)[0]
            subframe.grid(row=j, column=0)

def generar_word():
    with open("db.json", "r") as archivo:
        data = json.load(archivo)
    informacion = [Trabajador(**info) for info in data]

    with open("./plantillas/plantilla_oficio.txt", "r") as archivo:
        plantilla_oficio = archivo.read()

    for i, trabajador in enumerate(informacion):
        oficio = plantilla_oficio.format(
            nombre=trabajador.nombre,
            apellido1=trabajador.apellido1,
            apellido2=trabajador.apellido2,
            cargo=trabajador.cargo,
            empresa=trabajador.empresa,
            calle=trabajador.calle,
            numeroExt=trabajador.numeroExt,
            numeroInt=trabajador.numeroInt,
            colonia=trabajador.colonia,
            municipio=trabajador.municipio,
            estado=trabajador.estado,
            codigoPostal=trabajador.codigoPostal,
            telefono=trabajador.telefono,
            correoElectronico=trabajador.correoElectronico,
            fechaNacimiento=trabajador.fechaNacimiento,
            edad=trabajador.edad
        )
        
        # Crea un documento de Word en blanco
        document = docx.Document()

        # Agrega el texto al documento
        document.add_paragraph(oficio)

        # Guarda el documento en un archivo de Word
        nombre_archivo = f"./oficios/oficio_{i+1}.docx"
        document.save(nombre_archivo)

def generar_pdf():
    with open("db.json", "r") as archivo:
        data = json.load(archivo)
    informacion = [Trabajador(**info) for info in data]

    for i, trabajador in enumerate(informacion):
        pdf = cv.Canvas(f"./oficios/oficio_{i+1}.pdf", pagesize=letter)
        pdf.setTitle(f"Oficio_{i+1}")

        # Agrega el texto al PDF
        pdf.drawString(100, 750, f"Oficio {i+1}")
        pdf.drawString(100, 700, f"Nombre: {trabajador.nombre}")
        pdf.drawString(100, 650, f"Apellido 1: {trabajador.apellido1}")
        pdf.drawString(100, 600, f"Apellido 2: {trabajador.apellido2}")
        pdf.drawString(100, 550, f"Cargo: {trabajador.cargo}")
        pdf.drawString(100, 500, f"Empresa: {trabajador.empresa}")
        pdf.drawString(100, 450, f"Dirección: {trabajador.calle} {trabajador.numeroExt} {trabajador.numeroInt}, {trabajador.colonia}, {trabajador.municipio}, {trabajador.estado}, {trabajador.codigoPostal}")
        pdf.drawString(100, 400, f"Teléfono: {trabajador.telefono}")
        pdf.drawString(100, 350, f"Correo electrónico: {trabajador.correoElectronico}")
        pdf.drawString(100, 300, f"Fecha de nacimiento: {trabajador.fechaNacimiento}")
        pdf.drawString(100, 250, f"Edad: {trabajador.edad}")

        # Cierra el PDF
        pdf.save()

# Leer el archivo db.json
with open("db.json", "r") as f:
    data = json.load(f)

# Crear objetos Trabajador
trabajadores = []
for trabajador_data in data:
    trabajador = Trabajador(**trabajador_data)
    trabajadores.append(trabajador)

# Crear la interfaz
root = Tk()
root.title("Datos de Trabajadores")
root.geometry("450x500")

# Create the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the file menu
file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Agregar", menu=file_menu)

# Add menu items to the file menu
file_menu.add_command(label="Trabajador", command=lambda: os.system("python form.py"))
file_menu.add_command(label="Plantilla")

# Create the window menu
window_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Generar Oficios", menu=window_menu)

# Add menu items to the window menu
window_menu.add_command(label="Txt", command=generar_oficios)
window_menu.add_command(label="Word", command=generar_word)
window_menu.add_command(label="Pdf", command=generar_pdf)

# Create a canvas and a vertical scrollbar
canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame to contain the workers' data
frame = Frame(canvas)
canvas.create_window((0, 0), window=frame, anchor="nw")

for i, trabajador in enumerate(trabajadores):
    # Create a subframe for each worker
    subframe = Frame(frame, borderwidth=2, relief="groove", padx=10, pady=10)
    subframe.grid(row=i+1, column=0, padx=10, pady=10)


    # Crear los labels para mostrar los atributos del trabajador
    Label(subframe, text="Nombre:").grid(row=0, column=0, sticky="w")
    Label(subframe, text=trabajador.nombre).grid(row=0, column=1, sticky="w")

    Label(subframe, text="Apellido 1:").grid(row=1, column=0, sticky="w")
    Label(subframe, text=trabajador.apellido1).grid(row=1, column=1, sticky="w")

    Label(subframe, text="Apellido 2:").grid(row=2, column=0, sticky="w")
    Label(subframe, text=trabajador.apellido2).grid(row=2, column=1, sticky="w")

    Label(subframe, text="Cargo:").grid(row=3, column=0, sticky="w")
    Label(subframe, text=trabajador.cargo).grid(row=3, column=1, sticky="w")

    Label(subframe, text="Empresa:").grid(row=4, column=0, sticky="w")
    Label(subframe, text=trabajador.empresa).grid(row=4, column=1, sticky="w")

    Label(subframe, text="Calle:").grid(row=5, column=0, sticky="w")
    Label(subframe, text=trabajador.calle).grid(row=5, column=1, sticky="w")

    Label(subframe, text="Número exterior:").grid(row=6, column=0, sticky="w")
    Label(subframe, text=trabajador.numeroExt).grid(row=6, column=1, sticky="w")

    Label(subframe, text="Número interior:").grid(row=7, column=0, sticky="w")
    Label(subframe, text=trabajador.numeroInt).grid(row=7, column=1, sticky="w")

    Label(subframe, text="Colonia:").grid(row=8, column=0, sticky="w")
    Label(subframe, text=trabajador.colonia).grid(row=8, column=1, sticky="w")

    Label(subframe, text="Municipio:").grid(row=9, column=0, sticky="w")
    Label(subframe, text=trabajador.municipio).grid(row=9, column=1, sticky="w")

    Label(subframe, text="Estado:").grid(row=10, column=0, sticky="w")
    Label(subframe, text=trabajador.estado).grid(row=10, column=1, sticky="w")

    Label(subframe, text="Código Postal:").grid(row=11, column=0, sticky="w")
    Label(subframe, text=trabajador.codigoPostal).grid(row=11, column=1, sticky="w")

    Label(subframe, text="Teléfono:").grid(row=12, column=0, sticky="w")
    Label(subframe, text=trabajador.telefono).grid(row=12, column=1, sticky="w")

    Label(subframe, text="Correo electrónico:").grid(row=13, column=0, sticky="w")
    Label(subframe, text=trabajador.correoElectronico).grid(row=13, column=1, sticky="w")

    Label(subframe, text="Fecha de nacimiento:").grid(row=14, column=0, sticky="w")
    Label(subframe, text=trabajador.fechaNacimiento).grid(row=14, column=1, sticky="w")

    Label(subframe, text="Edad:").grid(row=15, column=0, sticky="w")
    Label(subframe, text=trabajador.edad).grid(row=15, column=1, sticky="w")

# Crear el botón de borrado y vincularlo a la función borrar_trabajador
    boton_borrar = Button(subframe, text="Borrar", command=lambda i=i: borrar_trabajador(i))
    boton_borrar.grid(row=16, column=0, sticky="e")
    # Crear el botón para abrir la interfaz de form.py
    boton_form = Button(subframe, text="Editar", command=lambda i=i: editar(i))
    boton_form.grid(row=16, column=1, sticky="s")
    
    boton_oficio = Button(subframe, text="Oficio", command=lambda i=i: generar_oficio(i))
    boton_oficio.grid(row=16, column=2, sticky="w")

frame.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Pack the canvas and start the main loop
canvas.pack(fill="both", expand=True)
root.mainloop()

