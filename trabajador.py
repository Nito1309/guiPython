import datetime

class Trabajador:        

    def __init__(self, nombre, apellido1, apellido2, cargo, empresa, calle, numeroExt, numeroInt, colonia, municipio, estado, codigoPostal, telefono, correoElectronico, fechaNacimiento, edad=None):
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.cargo = cargo
        self.empresa = empresa
        self.calle = calle
        self.numeroExt = numeroExt
        self.numeroInt = numeroInt
        self.colonia = colonia
        self.municipio = municipio
        self.estado = estado
        self.codigoPostal = codigoPostal
        self.telefono = telefono
        self.correoElectronico = correoElectronico

        self.fechaNacimiento = fechaNacimiento
        if edad is None:
            self.edad = self.calcular_edad()
        else:
            self.edad = edad

    def calcular_edad(self):
        fecha_actual = datetime.datetime.now().date()
        return fecha_actual.year - self.fechaNacimiento.year - ((fecha_actual.month, fecha_actual.day) < (self.fechaNacimiento.month, self.fechaNacimiento.day))
