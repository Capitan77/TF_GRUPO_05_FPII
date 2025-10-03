from models.base_empleado import Empleado

class Operario(Empleado):
    def get_cargo(self):
        return "Operario"

    def calcular_pago(self):
        return round(self.get_sueldo_base(), 2)