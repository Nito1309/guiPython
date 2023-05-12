import json
import os
import datetime
from trabajador import Trabajador

# PATHS
PLANTILLAS = './plantillas'
OFICIOS = './oficios'
DB_PATH = 'db.json'

def solicitar_informacion():
    nombre = input("Nombre: ")
    apellido1 = input("Primer apellido: ")
    apellido2 = input("Segundo apellido: ")
    cargo = input("Cargo: ")
    empresa = input("Empresa: ")
    calle = input("Calle: ")
    numero_exterior = input("Número exterior: ")
    numero_interior = input("Número interior: ")
    colonia = input("Colonia: ")
    municipio = input("Municipio: ")
    estado = input("Estado: ")
    codigo_postal = input("Código postal: ")
    telefono = input("Teléfono: ")
    correo_electronico = input("Correo electrónico: ")
    fecha_nacimiento = input("Fecha de nacimiento (formato: AAAA-MM-DD): ")
    
    fecha_actual = datetime.datetime.now().date()
    fecha_nac = datetime.datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    fecha_nacimiento = fecha_nac.strftime("%Y-%m-%d")
    edad = fecha_actual.year - fecha_nac.year - ((fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day))
    
    trabajador = Trabajador(nombre, apellido1, apellido2, cargo, empresa, calle, numero_exterior,
                            numero_interior, colonia, municipio, estado, codigo_postal, telefono,
                            correo_electronico, fecha_nacimiento, edad)
    
    return trabajador


if os.path.exists(DB_PATH):
    agregar_informacion = input("¿Desea agregar información al archivo? (s/n) ")
    if agregar_informacion.lower() == "s":
        with open(DB_PATH, "r") as archivo:
            informacion_existente = json.load(archivo)

        informacion_nueva = solicitar_informacion()

        # Convertir objeto Trabajador en diccionario
        informacion_nueva = informacion_nueva.__dict__

        informacion_existente.append(informacion_nueva)

        with open(DB_PATH, "w") as archivo:
            json.dump(informacion_existente, archivo)
    else:
        print("La información existente no será modificada")
else:
    trabajador = solicitar_informacion()

    # Convertir objeto Trabajador en diccionario
    informacion = [trabajador.__dict__]

    with open(DB_PATH, "w") as archivo:
        json.dump(informacion, archivo)

with open(DB_PATH, "r") as archivo:
    data = json.load(archivo)

informacion = [Trabajador(**info) for info in data]

with open(PLANTILLAS+"/plantilla_oficio.txt", "r") as archivo:
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
    
    nombre_archivo = f"{OFICIOS}/oficio_{i+1}.txt"
    with open(nombre_archivo, "w") as archivo:
        archivo.write(oficio)

print("Oficios creados correctamente")
