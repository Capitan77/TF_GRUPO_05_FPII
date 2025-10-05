# Capa de aplicación (UI por consola).
# Orquesta las opciones del menú y usa el repositorio + clases de dominio.

from models.operario import Operario
from models.vendedor import Vendedor
from models.supervisor import Supervisor
from models.administrador import Administrador
from repository.repositorio import EmpleadosRepo

# Catálogos simples que se muestran al usuario para elegir.
#opciones a seleccionar de todas las áreas
AREAS = ["Producción", "Distribución", "Ventas", "Recursos Humanos"]
#opciones a seleccionar de todos los cargos
CARGOS = ["Operario", "Vendedor", "Supervisor", "Administrador"]

#inicializamos la clase app donde mostraremos en terminal el sistema
class App:
    #inicializamos abriendo un repositorio para los empleados
    def __init__(self):
        # Repositorio en memoria que almacena a todos los empleados
        self.repo = EmpleadosRepo()

    #menu servira para imprimir las opciones en terminal
    def menu(self):
    
        #Menú principal: imprime opciones y llama a la acción correspondiente.
        #Se repite hasta que el usuario selecciona '0. Salir'.
       
       #mientra el bucle sea verdadero se ejecutara el sistema una y otra vez
        while True:
            #brindando opciones de la GUI 
            print("\nSISTEMA DE GESTIÓN D'ONOFRIO\n")
            print("1. Registrar empleado")
            print("2. Listar empleados")
            print("3. Registrar asistencia")
            print("4. Registrar venta")
            print("5. Calcular planilla")
            print("0. Salir\n")
            #almacenas en una variable por medio de un input el 
            #numero de opcion que queremos manejar
            opcion = input("Seleccione una opción: ").strip()

            #usamos if, elif para llamar a los metodos respectivos 
            #para cada funcion de app
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
    
    #funcion para registrar empleados ingresados
    def registrar_empleado(self):
       
        #Crea un empleado según el cargo elegido y lo guarda en el repositorio.
        #Demuestra ABSTRACCIÓN (usamos la interfaz común) y HERENCIA/POLIMORFISMO
        #(instanciamos subclases distintas según el cargo).
        
        #almacena en variables el dni y nombre de empleado ingresado por medio de inputs
        dni = input("DNI (8 dígitos): ")
        nombre = input("Nombre completo: ")

        # Elegir cargo de la lista
        print("\nSeleccione el Cargo:")
        #for con 2 valores que recorreran todo el array de cargos 
        # donde retornará la posicion y el nombre del cargo
        for i, cargo in enumerate(CARGOS, 1):
            #imprimir posicion y cargo
            print(f"{i}. {cargo}")
            #restamos con uno la posicion ingresa en input porque el 
            #array trabajo las posiciones desde el 0
        cargo = CARGOS[int(input("Opción: ")) - 1]

        # Elegir área de la lista
        print("\nSeleccione el Área:")
        #for con 2 valores que recorreran todo el array de cargos 
        # donde retornará la posicion y el nombre del area
        for i, area in enumerate(AREAS, 1):
            #imprimir posicion y area
            print(f"{i}. {area}")
            #restamos con uno la posicion ingresa en input porque el 
            #array trabajo las posiciones desde el 0
        area = AREAS[int(input("Opción: ")) - 1]
        #ingresamos el sueldo por medio de un input
        sueldo = float(input("Sueldo Base: "))

        # Creamos la instancia concreta según el cargo (POLIMORFISMO)
        # depediendo del cargo por medio de un if, elif almacenamos los datos
        #ingresados determinando el campo segun su cargo
        if cargo == "Operario":
            emp = Operario(dni, nombre, area, sueldo)
        elif cargo == "Vendedor":
            emp = Vendedor(dni, nombre, area, sueldo)
        elif cargo == "Supervisor":
            emp = Supervisor(dni, nombre, area, sueldo)
        else:
            emp = Administrador(dni, nombre, area, sueldo)

        # Guardamos en el repositorio
        #usamos try y except para evitar algun posible error
        try:
            #llamamos al metodo de repositorio.py para agregar y guardar al empleado
            self.repo.agregar(emp)
            print("Empleado registrado correctamente.")
            #encaso algo este mal por medio de except se captara el error 
            #y este avisara
        except ValueError as e:
            print("Error:", e)

    def listar_empleados(self):
     
        #Muestra los empleados en formato MULTILÍNEA (más legible),
        #cumpliendo con el requerimiento de no listarlos en una sola línea.
       
       #llamamos al metodo del repositorio listar para poder mostrar los empleados ingresados
        empleados = self.repo.listar()
        #si no hay empleados entonces returnamos 
        if not empleados:
            print("No hay empleados registrados.")
            return
        #en caso si, comenzamos con la impresion de cada uno de los datos del trabajor
        print("\n--- LISTADO DE EMPLEADOS ---")
        for emp in empleados:
            print(f"DNI: {emp.get_dni()}")
            print(f"Nombre: {emp.get_nombre()}")
            print(f"Cargo: {emp.get_cargo()}")
            print(f"Área: {emp.get_area()}")
            print(f"Sueldo Base: {emp.get_sueldo_base():.2f}")
            print(f"Asistencias: {emp.get_asistencias()}")
            # en caso sea un vendedor se mostrara la comision acumulada
            if emp.get_cargo() == "Vendedor":
                # Solo los vendedores acumulan comisión por ventas
                print(f"Comisiones: {emp.get_comision():.2f}")
            print("-----------------------------")

    #metodo para registrar las asistencias que tiene cada uno de los empleados
    def registrar_asistencia(self):
     
        #Suma 1 asistencia al empleado encontrado por DNI.
        #Usa ENCAPSULAMIENTO: no tocamos atributos, llamamos al método público.
       
        #pedimos por medio de un input el dni para reconocer al empleado
        dni = input("Ingrese DNI: ")
        #llamamos al metodo obtener de repositorio para obtener al empleado por medio del dni
        emp = self.repo.obtener(dni)
        #si el empleado esta registrado entonces se llamar al metodo de registrar asistencias 
        #de base_empleado
        if emp:
            emp.registrar_asistencia()
            print("Asistencia registrada para", emp.get_nombre())
        #en caso no, se indicara que no se encontro
        else:
            print("Empleado no encontrado.")

    def registrar_venta(self):
      
        #Registra una venta SOLO si el empleado es Vendedor.
        #La comisión (5%) se calcula dentro de la clase 'Vendedor'
        #y se acumula mediante un método protegido (_sumar_comision).
       
        #ingresa el dni para buscar al vendedor 
        dni = input("Ingrese DNI: ")
        #entra al repositorio buscando al empleado que coincida con el codigo y el cargo vendedor
        emp = self.repo.obtener(dni)
        #si coincide almacena en variable monto el valor permitido a ingresar
        if emp and emp.get_cargo() == "Vendedor":
            monto = float(input("Monto de la venta: "))
            # Llama a la lógica específica de Vendedor
            emp.registrar_venta(monto)  
            print("Venta registrada. Comisión actual:", emp.get_comision())
        else:
            print("Empleado no encontrado o no es Vendedor.")

    def calcular_planilla(self):
      
        #Recorre todos los empleados y llama a su método polimórfico 'calcular_pago'.
        #Cada subclase puede definir su propio cálculo (Vendedor incluye comisiones).
       
       #llamamos al metodo listar de repositorio y mantenemos en empleados
        empleados = self.repo.listar()
        #si no hay empleados entonces se imprimira que no se encontro empleados
        if not empleados:
            print("No hay empleados registrados.")
            return
        #en caso si, se abrira un for para recorrer cada empleado registrado 
        print("\n--- PLANILLA ---")
        for emp in empleados:
            #se llamara al metodo calcular pago de cada subclase empleado donde se trabajan de 
            #diferente manera y te igualaran a total
            total = emp.calcular_pago()  # POLIMORFISMO
            #finalmente se imprime el nombre, cargo y su planilla
            print(f"{emp.get_nombre()} ({emp.get_cargo()}) → Total a pagar: S/. {total:.2f}")