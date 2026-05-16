from tasks_cli import storage
from tasks_cli import tasks as task_ops


def _prompt_choice() -> str:
    print()
    print("1) Agregar tarea")
    print("2) Listar tareas")
    print("3) Marcar tarea como completada")
    print("4) Eliminar tarea")
    print("5) Editar título de tarea")
    print("6) Buscar tareas por texto")
    print("7) Salir")
    return input("Elegí una opción: ").strip()


def _prompt_task_id() -> int | None:
    raw = input("ID de la tarea: ").strip()
    if not raw:
        return None
    try:
        return int(raw)
    except ValueError:
        return None


def _list_tasks(task_list: list[dict]) -> None:
    if not task_list:
        print("No hay tareas.")
        return
    for task in task_list:
        tid = task.get("id", "?")
        title = task.get("title", "")
        completed = bool(task.get("completed", False))
        estado = "sí" if completed else "no"
        print(f"[{tid}] {title} — completada: {estado}")


def main() -> None:
    task_list = storage.load_tasks()

    while True:
        choice = _prompt_choice()

        if choice == "1":
            title = input("Título de la tarea: ").strip()
            if not title:
                print("El título no puede estar vacío.")
                continue
            task_ops.add_task(task_list, title)
            storage.save_tasks(task_list)
            print("Tarea agregada.")

        elif choice == "2":
            _list_tasks(task_list)

        elif choice == "3":
            task_id = _prompt_task_id()
            if task_id is None:
                print("ID inválido.")
                continue
            result = task_ops.complete_task(task_list, task_id)
            if result == "completed":
                storage.save_tasks(task_list)
                print("Tarea marcada como completada.")
            elif result == "already_completed":
                print("La tarea ya estaba completada.")
            else:
                print("No se encontró una tarea con ese ID.")

        elif choice == "4":
            task_id = _prompt_task_id()
            if task_id is None:
                print("ID inválido.")
                continue
            if task_ops.delete_task(task_list, task_id):
                storage.save_tasks(task_list)
                print("Tarea eliminada.")
            else:
                print("No se encontró una tarea con ese ID.")

        elif choice == "5":
            task_id = _prompt_task_id()
            if task_id is None:
                print("ID inválido.")
                continue
            new_title = input("Nuevo título: ").strip()
            if not new_title:
                print("El título no puede estar vacío.")
                continue
            result = task_ops.edit_task(task_list, task_id, new_title)
            if result == "edited":
                storage.save_tasks(task_list)
                print("Título actualizado.")
            elif result == "unchanged":
                print("El título no cambió.")
            else:
                print("No se encontró una tarea con ese ID.")

        elif choice == "6":
            query = input("Texto a buscar: ").strip()
            if not query:
                print("El texto de búsqueda no puede estar vacío.")
                continue
            matches = task_ops.search_tasks(task_list, query)
            if not matches:
                print("No se encontraron tareas con ese texto.")
            else:
                _list_tasks(matches)

        elif choice == "7":
            print("Chau.")
            break

        else:
            print("Opción no válida.")
