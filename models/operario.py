# Subclase de Empleado.
# Implementa su propio cargo y el cálculo de pago.

from models.base_empleado import Empleado

class Operario(Empleado):
    def get_cargo(self):
        return "Operario"

    def calcular_pago(self):
        # Operario cobra solo sueldo base (por ahora)
        return round(self.get_sueldo_base(), 2)