# Punto de entrada del programa.
# Solo crea una instancia de App y lanza el menú de opciones.

from app.app import App  # Importamos la clase App desde el paquete app

if __name__ == "__main__":
    sistema = App()   # Creamos el sistema
    sistema.menu()    # Mostramos el menú interactivo en consola