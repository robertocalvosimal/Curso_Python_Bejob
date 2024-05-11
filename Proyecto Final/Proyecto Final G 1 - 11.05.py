class Tarea:
    """
    Clase que representa una tarea pendiente.

    Atributos:
        descripcion (str): La descripción de la tarea.
        estado (bool): True si la tarea está completada, False en caso contrario.
    """

    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.estado = False

    def marcar_completada(self):
        """
        Marca la tarea como completada si no lo está.
        """
        self.estado = True

    def __str__(self):
        """
        Devuelve una cadena que representa la tarea.
        """
        if self.estado:
            estado = "Completada"
        else:
            estado = "Pendiente"
        return f"- {self.descripcion} ({estado})"


class GestorTareas:
    """
    Clase que gestiona una lista de tareas pendientes.

    Atributos:
        tareas (list): La lista de tareas pendientes.
    """

    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        """
        Agrega una nueva tarea a la lista.
        """
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea agregada: {nueva_tarea}")

    def marcar_completada(self, posicion):
        """
        Marca una tarea como completada dada su posición en la lista.
        """
        try:
            tarea = self.tareas[posicion - 1]
            if not tarea.estado:
                tarea.marcar_completada()
                mensaje = f"Tarea en la posición {posicion} completada: {tarea.descripcion}"
            else:
                mensaje = f"La tarea '{tarea.descripcion}' en la posición {posicion} ya está completada."
            print(mensaje)
        except IndexError:
            print(f"Error: La posición {posicion} no existe.")

    def mostrar_tareas(self):
        """
        Muestra todas las tareas en la lista.
        """
        if not self.tareas:
            print("No hay tareas pendientes.")
            return

        print("\nLista de tareas:")
        for i, tarea in enumerate(self.tareas):
            print(f"{i + 1}. {tarea}")

    def eliminar_tarea(self, posicion):
        """
        Elimina una tarea de la lista dada su posición.
        """
        try:
            del self.tareas[posicion - 1]
            print(f"Tarea en la posición {posicion} eliminada.")
        except IndexError:
            print(f"Error: La posición {posicion} no existe.")


def main():
    gestor_tareas = GestorTareas()

    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Eliminar tarea")
        print("5. Salir")

        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError:
            print("Opción no válida. Ingrese un número entero.")
            continue

        if opcion == 1:
            descripcion = input("Ingrese la descripción de la tarea: ")
            gestor_tareas.agregar_tarea(descripcion)
        elif opcion == 2:
            posicion = int(input("Ingrese la posición de la tarea a completar: "))
            gestor_tareas.marcar_completada(posicion)
        elif opcion == 3:
            gestor_tareas.mostrar_tareas()
        elif opcion == 4:
            posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
            gestor_tareas.eliminar_tarea(posicion)
        elif opcion == 5:
            print("Saliendo del gestor de tareas...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()