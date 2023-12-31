class Asiento:
    
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro
    
    def cambiarColor(self, nuevoColor):
        if (nuevoColor == "rojo" or nuevoColor == "verde" or nuevoColor == "amarillo" or nuevoColor == "negro" or nuevoColor == 'blanco'):
            self.color = str(nuevoColor)


class Motor:

    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro
    
    def cambiarRegistro(self, nuevoRegistro):
        self.registro = int(nuevoRegistro)
    
    def asignarTipo(self, nuevoTipo):
        if (nuevoTipo == "electrico" or nuevoTipo == "gasolina"):
            self.tipo = str(nuevoTipo)

class Auto:
    
    cantidadCreados = 0

    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.Asiento = asientos
        self.marca = marca
        self.Motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):
        count = 0
        if self.asientos != 0:
            for i in self.asientos:
                if isinstance (i,Asiento):
                    count += 1
        return count
    
    def verificarIntegridad(self):
        if self.registro == self.Motor.registro:
            if self.Asiento != 0:
                for i in self.Asiento:
                    if isinstance (i,Asiento):
                        if self.registro != i.registro:
                            return "Las piezas no son originales"
            return "Auto original"                
        return "Las piezas no son originales"





        
        



