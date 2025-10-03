# Subclase de Empleado.

from models.base_empleado import Empleado

class Administrador(Empleado):
    def get_cargo(self):
        return "Administrador"

    def calcular_pago(self):
        return round(self.get_sueldo_base(), 2)