# Subclase de Empleado.
# Tiene un método adicional: registrar_venta, que suma comisión (5%).

from models.base_empleado import Empleado

class Vendedor(Empleado):
    def get_cargo(self):
        return "Vendedor"

    def registrar_venta(self, monto):
        """
        Suma 5% del monto vendido a su comisión acumulada.
        """
        if monto > 0:
            comision = round(monto * 0.05, 2)
            self._sumar_comision(comision)

    def calcular_pago(self):
        # Total = sueldo base + comisión acumulada
        return round(self.get_sueldo_base() + self.get_comision(), 2)