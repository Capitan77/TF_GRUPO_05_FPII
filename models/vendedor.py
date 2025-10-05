# Subclase de Empleado.
# Tiene un método adicional: registrar_venta, que suma comisión (5%).

from models.base_empleado import Empleado

class Vendedor(Empleado):

    #al no colocar el def __init__, de igual manera como si lo pusieramos los
    #atributos de la clase padre ya quedan inicializados

    #declaramos un metodo que retorne unicamente la definicion del cargo
    #que esta desempeñando el empleado 
    def get_cargo(self):
        return "Vendedor"

    # se conecta con registra venta de app, desde donde esta recibiendo el valor del monto
    # para la operacion 
    def registrar_venta(self, monto):
        """
        Suma 5% del monto vendido a su comisión acumulada.
        """
        #si el monto recibido de app es mayor a 0 entonces se ejecuta la siguiente operacion
        if monto > 0:
            comision = round(monto * 0.05, 2)
            #y se llama al metodo de base_empleado donde se suma la comision del vendedor por venta
            self._sumar_comision(comision)

    def calcular_pago(self):
        # Total = sueldo base + comisión acumulada
        return round(self.get_sueldo_base() + self.get_comision(), 2)