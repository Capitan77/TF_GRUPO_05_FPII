# Capa de aplicación (UI por consola).
# Orquesta las opciones del menú y usa el repositorio + clases de dominio.

from models.operario import Operario
from models.vendedor import Vendedor
from models.supervisor import Supervisor
from models.administrador import Administrador
from repository.repositorio import EmpleadosRepo

# Catálogos simples que se muestran al usuario para elegir.
AREAS = ["Producción", "Distribución", "Ventas", "Recursos Humanos"]
CARGOS = ["Operario", "Vendedor", "Supervisor", "Administrador"]

class App:
    def __init__(self):
        # Repositorio en memoria que almacena a todos los empleados
        self.repo = EmpleadosRepo()

    def menu(self):
        """
        Menú principal: imprime opciones y llama a la acción correspondiente.
        Se repite hasta que el usuario selecciona '0. Salir'.
        """
        while True:
            print("\nSISTEMA DE GESTIÓN D'ONOFRIO\n")
            print("1. Registrar empleado")
            print("2. Listar empleados")
            print("3. Registrar asistencia")
            print("4. Registrar venta")
            print("5. Calcular planilla")
            print("0. Salir\n")
            opcion = input("Seleccione una opción: ").strip()

            if opcion == "1":
                self.registrar_empleado()
            elif opcion == "2":
                self.listar_empleados()
            elif opcion == "3":
                self.registrar_asistencia()
            elif opcion == "4":
                self.registrar_venta()
            elif opcion == "5":
                self.calcular_planilla()
            elif opcion == "0":
                print("Saliendo del sistema")
                break
            else:
                print("Opción inválida.")

    def registrar_empleado(self):
        """
        Crea un empleado según el cargo elegido y lo guarda en el repositorio.
        Demuestra ABSTRACCIÓN (usamos la interfaz común) y HERENCIA/POLIMORFISMO
        (instanciamos subclases distintas según el cargo).
        """
        dni = input("DNI (8 dígitos): ")
        nombre = input("Nombre completo: ")

        # Elegir cargo de la lista
        print("\nSeleccione el Cargo:")
        for i, cargo in enumerate(CARGOS, 1):
            print(f"{i}. {cargo}")
        cargo = CARGOS[int(input("Opción: ")) - 1]

        # Elegir área de la lista
        print("\nSeleccione el Área:")
        for i, area in enumerate(AREAS, 1):
            print(f"{i}. {area}")
        area = AREAS[int(input("Opción: ")) - 1]

        sueldo = float(input("Sueldo Base: "))

        # Creamos la instancia concreta según el cargo (POLIMORFISMO)
        if cargo == "Operario":
            emp = Operario(dni, nombre, area, sueldo)
        elif cargo == "Vendedor":
            emp = Vendedor(dni, nombre, area, sueldo)
        elif cargo == "Supervisor":
            emp = Supervisor(dni, nombre, area, sueldo)
        else:
            emp = Administrador(dni, nombre, area, sueldo)

        # Guardamos en el repositorio
        try:
            self.repo.agregar(emp)
            print("Empleado registrado correctamente.")
        except ValueError as e:
            print("Error:", e)

    def listar_empleados(self):
        """
        Muestra los empleados en formato MULTILÍNEA (más legible),
        cumpliendo con el requerimiento de no listarlos en una sola línea.
        """
        empleados = self.repo.listar()
        if not empleados:
            print("No hay empleados registrados.")
            return
        print("\n--- LISTADO DE EMPLEADOS ---")
        for emp in empleados:
            print(f"DNI: {emp.get_dni()}")
            print(f"Nombre: {emp.get_nombre()}")
            print(f"Cargo: {emp.get_cargo()}")
            print(f"Área: {emp.get_area()}")
            print(f"Sueldo Base: {emp.get_sueldo_base():.2f}")
            print(f"Asistencias: {emp.get_asistencias()}")
            if emp.get_cargo() == "Vendedor":
                # Solo los vendedores acumulan comisión por ventas
                print(f"Comisiones: {emp.get_comision():.2f}")
            print("-----------------------------")

    def registrar_asistencia(self):
        """
        Suma 1 asistencia al empleado encontrado por DNI.
        Usa ENCAPSULAMIENTO: no tocamos atributos, llamamos al método público.
        """
        dni = input("Ingrese DNI: ")
        emp = self.repo.obtener(dni)
        if emp:
            emp.registrar_asistencia()
            print("Asistencia registrada para", emp.get_nombre())
        else:
            print("Empleado no encontrado.")

    def registrar_venta(self):
        """
        Registra una venta SOLO si el empleado es Vendedor.
        La comisión (5%) se calcula dentro de la clase 'Vendedor'
        y se acumula mediante un método protegido (_sumar_comision).
        """
        dni = input("Ingrese DNI: ")
        emp = self.repo.obtener(dni)
        if emp and emp.get_cargo() == "Vendedor":
            monto = float(input("Monto de la venta: "))
            emp.registrar_venta(monto)  # Llama a la lógica específica de Vendedor
            print("Venta registrada. Comisión actual:", emp.get_comision())
        else:
            print("Empleado no encontrado o no es Vendedor.")

    def calcular_planilla(self):
        """
        Recorre todos los empleados y llama a su método polimórfico 'calcular_pago'.
        Cada subclase puede definir su propio cálculo (Vendedor incluye comisiones).
        """
        empleados = self.repo.listar()
        if not empleados:
            print("No hay empleados registrados.")
            return
        print("\n--- PLANILLA ---")
        for emp in empleados:
            total = emp.calcular_pago()  # POLIMORFISMO
            print(f"{emp.get_nombre()} ({emp.get_cargo()}) → Total a pagar: S/. {total:.2f}")