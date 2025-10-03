from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, dni, nombre, area, sueldo_base):
        self.__dni = dni
        self.__nombre = nombre
        self.__area = area
        self.__sueldo_base = sueldo_base
        self.__asistencias = 0
        self.__comision_acumulada = 0.0

    def get_dni(self):
        return self.__dni

    def get_nombre(self):
        return self.__nombre

    def get_area(self):
        return self.__area

    def get_sueldo_base(self):
        return self.__sueldo_base

    def get_asistencias(self):
        return self.__asistencias

    def get_comision(self):
        return self.__comision_acumulada

    def registrar_asistencia(self):
        self.__asistencias += 1

    def _sumar_comision(self, monto):
        self.__comision_acumulada += monto

    @abstractmethod
    def calcular_pago(self):
        pass

    @abstractmethod
    def get_cargo(self):
        pass