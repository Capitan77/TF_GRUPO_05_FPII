# Repositorio simple en memoria.
# Responsable de ALMACENAR, BUSCAR y LISTAR empleados.

class EmpleadosRepo:
    def __init__(self):
        # Diccionario: clave = DNI, valor = instancia de Empleado (o subclase)
        self.empleados = {}
    
    #necesitamos de un parametro que retorne al empleado para agregarlo a la lista
    def agregar(self, empleado):
        
        #Inserta un empleado nuevo. Lanza error si el DNI ya existe.
        
        if empleado.get_dni() in self.empleados:
            raise ValueError("Ya existe un empleado con ese DNI.")
        self.empleados[empleado.get_dni()] = empleado

    def obtener(self, dni):
       
        #Devuelve el empleado por DNI, o None si no existe.
       
        return self.empleados.get(dni)

    def listar(self):
       
        #Retorna la lista (copia) de empleados almacenados.
        
        return list(self.empleados.values())