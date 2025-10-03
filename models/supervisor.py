from models.base_empleado import Empleado

class Supervisor(Empleado):
    def get_cargo(self):
        return "Supervisor"

    def calcular_pago(self):
        return round(self.get_sueldo_base(), 2)