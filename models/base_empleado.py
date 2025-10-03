# Clase abstracta base. Define la interfaz común para todos los empleados.
# Aquí se demuestra ENCAPSULAMIENTO (atributos privados) y ABSTRACCIÓN.

from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, dni, nombre, area, sueldo_base):
        # Atributos privados (doble guión bajo) → no se acceden directo desde fuera.
        self.__dni = dni
        self.__nombre = nombre
        self.__area = area
        self.__sueldo_base = sueldo_base
        self.__asistencias = 0
        self.__comision_acumulada = 0.0

    # ----- Getters (lectura segura de los atributos privados) -----
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

    # ----- Comportamientos comunes para todos los empleados -----
    
    def registrar_asistencia(self):
        # Aumenta en 1 las asistencias del empleado
        self.__asistencias += 1

    # Método protegido: solo las subclases deberían usarlo para acumular comisión
    def _sumar_comision(self, monto):
        self.__comision_acumulada += monto

    # ----- Métodos abstractos (cada subclase los implementa a su manera) -----
    @abstractmethod
    def calcular_pago(self):
        """
        Retorna el total a pagar. Vendedor suma comisiones, otros no.
        """
        pass

    @abstractmethod
    def get_cargo(self):
        """
        Devuelve el nombre del cargo (Operario, Vendedor, etc.).
        """
        pass