# Subclase de Empleado (misma lógica de pago que Operario/Administrador por ahora).

from models.base_empleado import Empleado

class Supervisor(Empleado):

    #al no colocar el def __init__, de igual manera como si lo pusieramos los
    #atributos de la clase padre ya quedan inicializados
    
    #declaramos un metodo que retorne unicamente la definicion del cargo
    #que esta desempeñando el empleado
    def get_cargo(self):
        return "Supervisor"

    def calcular_pago(self):
        return round(self.get_sueldo_base(), 2)