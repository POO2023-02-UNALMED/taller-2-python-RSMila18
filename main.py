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
        Asiento = asientos
        self.marca = marca
        Motor = motor
        self.registro = registro
        

    def cantidadAsientos(self):
        count = 0
        asientos = [Asiento(self)]

        for i in range(len(asientos)):
            if asientos[i] != 0 or asientos[i] != None:
                count =+ 1
            
        return count
    
    def verificarIntegridad(self):
        asientos = [Asiento(self)]
        
        for i in range(len(asientos)):
            if asientos[i] != 0 or asientos[i] != None:
                if asientos[i].registro == (Auto(self).registro and Motor(self).registro):
                 return "Auto original"
            else:
                return "Las piezas del auto no son originales"





        
        



