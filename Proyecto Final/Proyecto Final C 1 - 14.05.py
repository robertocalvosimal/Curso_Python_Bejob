class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True

    def __str__(self):
        estado = "Completada" if self.completada else "Pendiente"
        return f"{self.descripcion} - {estado}"


class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, descripcion):
        nueva_tarea = Tarea(descripcion)
        self.tareas.append(nueva_tarea)
        print(f"Tarea '{descripcion}' agregada.")

    def marcar_completada(self, posicion):
        try:
            self.tareas[posicion].marcar_completada()
            print(f"Tarea en posición {posicion} marcada como completada.")
        except IndexError:
            print("Error: Posición no válida.")

    def mostrar_tareas(self):
        if not self.tareas:
            print("No hay tareas en la lista.")
        else:
            for i, tarea in enumerate(self.tareas):
                print(f"{i}. {tarea}")

    def eliminar_tarea(self, posicion):
        try:
            tarea_eliminada = self.tareas.pop(posicion)
            print(f"Tarea '{tarea_eliminada.descripcion}' eliminada.")
        except IndexError:
            print("Error: Posición no válida.")


def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar tarea")
    print("2. Marcar tarea como completada")
    print("3. Mostrar todas las tareas")
    print("4. Eliminar tarea")
    print("5. Salir")


def main():
    lista_tareas = ListaTareas()
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            descripcion = input("Ingrese la descripción de la tarea: ")
            lista_tareas.agregar_tarea(descripcion)
        elif opcion == "2":
            try:
                posicion = int(input("Ingrese la posición de la tarea a marcar como completada: "))
                lista_tareas.marcar_completada(posicion)
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        elif opcion == "3":
            lista_tareas.mostrar_tareas()
        elif opcion == "4":
            try:
                posicion = int(input("Ingrese la posición de la tarea a eliminar: "))
                lista_tareas.eliminar_tarea(posicion)
            except ValueError:
                print("Error: Debe ingresar un número entero.")
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()