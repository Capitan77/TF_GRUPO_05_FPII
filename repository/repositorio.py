class EmpleadosRepo:
    def __init__(self):
        self.empleados = {}

    def agregar(self, empleado):
        if empleado.get_dni() in self.empleados:
            raise ValueError("Ya existe un empleado con ese DNI.")
        self.empleados[empleado.get_dni()] = empleado

    def obtener(self, dni):
        return self.empleados.get(dni)

    def listar(self):
        return list(self.empleados.values())