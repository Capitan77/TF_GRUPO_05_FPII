# Subclase de Empleado.
# Implementa su propio cargo y el cálculo de pago.

from models.base_empleado import Empleado

class Operario(Empleado):

    #al no colocar el def __init__, de igual manera como si lo pusieramos los
    #atributos de la clase padre ya quedan inicializados

    #declaramos un metodo que retorne unicamente la definicion del cargo
    #que esta desempeñando el empleado
    def get_cargo(self):
        return "Operario"

    def calcular_pago(self):
        # Operario cobra solo sueldo base (por ahora) con 2 decimales
        return round(self.get_sueldo_base(), 2)