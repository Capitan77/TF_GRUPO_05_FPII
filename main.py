# Punto de entrada del programa.
# Solo crea una instancia de App y lanza el menú de opciones.

from app.app import App  # Importamos la clase App desde el paquete app

if __name__ == "__main__":
    sistema = App()   # de la clase app creamos una "app" llamada sistema
    sistema.menu()    # y llamamos al metodo que inicializara el sistema 
    # por medio del metodo menu(), el cual le pertenece a sistema creada de app()