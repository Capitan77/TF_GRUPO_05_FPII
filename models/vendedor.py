from models.base_empleado import Empleado

class Vendedor(Empleado):
    def get_cargo(self):
        return "Vendedor"

    def registrar_venta(self, monto):
        if monto > 0:
            comision = round(monto * 0.05, 2)
            self._sumar_comision(comision)

    def calcular_pago(self):
        return round(self.get_sueldo_base() + self.get_comision(), 2)