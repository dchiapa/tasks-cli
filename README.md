# tasks-cli

Aplicación de consola en Python para gestionar tareas simples. Usa solo la librería estándar y persiste los datos en `tasks.json` en la raíz del proyecto.

## Versión actual

`1.3.0` — definida en `tasks_cli.__version__`.

## Requisitos

- Python 3.10 o superior
- Git (solo para clonar el repositorio)

No se requieren dependencias externas ni `pip install`: la aplicación usa únicamente la librería estándar de Python.

## Instalación

Cloná el repositorio y entrá al directorio del proyecto:

```bash
git clone https://github.com/dchiapa/tasks-cli.git
cd tasks-cli
```

Con SSH:

```bash
git clone git@github.com:dchiapa/tasks-cli.git
cd tasks-cli
```

Verificá que tenés una versión compatible de Python:

```bash
# Linux / macOS
python3 --version

# Windows (PowerShell o CMD)
python --version
```

## Uso

Ejecutá la aplicación **desde la raíz del proyecto** (donde está la carpeta `tasks_cli/`):

```bash
# Linux / macOS
python3 -m tasks_cli

# Windows
python -m tasks_cli
```

Se abrirá el menú interactivo por consola. Los datos se guardan en `tasks.json` en esa misma carpeta (el archivo se crea al guardar la primera tarea).

## Pruebas

Para correr la suite de pruebas, también desde la raíz del proyecto:

```bash
# Linux / macOS
python3 -m unittest discover -s tests -v

# Windows
python -m unittest discover -s tests -v
```

Salida esperada al final: `OK` y el total de tests ejecutados (20 en la versión `1.3.0`).

## Estructura

```text
tasks-cli/
├── .cursor/
│   └── rules/
│       └── project.mdc
├── tasks_cli/             # Código de la aplicación
├── tests/                 # Pruebas automatizadas
├── tasks.json             # Datos locales (generado en ejecución, no versionado)
├── .gitattributes
├── .gitignore
└── README.md
```

## Modelo de datos

Cada tarea se guarda como un objeto JSON con tres campos:

| Campo       | Tipo    | Descripción                          |
|------------|---------|--------------------------------------|
| `id`       | entero  | Identificador único autoincremental  |
| `title`    | texto   | Título de la tarea                   |
| `completed`| booleano| `true` si está completada            |

El archivo `tasks.json` contiene una lista de esos objetos.

---

## Versionado (SemVer)

Este proyecto sigue [Versionado Semántico 2.0.0](https://semver.org/lang/es/): `MAYOR.MENOR.PARCHE`.

| Componente | Cuándo incrementarlo en tasks-cli                         |
|------------|-----------------------------------------------------------|
| **MAYOR**  | Cambios incompatibles (p. ej. nuevo formato de `tasks.json`) |
| **MENOR**  | Funcionalidad nueva compatible con versiones anteriores   |
| **PARCHE** | Correcciones de bugs sin cambiar el comportamiento esperado |

Estado de cada release: **publicada** (disponible) o **planificada** (definida, sin implementar).

| Versión   | Estado      | Resumen                                      |
|-----------|-------------|----------------------------------------------|
| `1.3.0`   | Publicada   | Nomenclatura alineada al repo (`tasks-cli`)  |
| `1.2.0`   | Publicada   | Suite de pruebas automatizadas (`unittest`)  |
| `1.1.0`   | Publicada   | Editar título y buscar tareas por texto      |
| `1.0.0`   | Publicada   | CRUD básico, menú por consola, persistencia  |

> Un **`2.0.0`** se reservaría para cambios incompatibles (p. ej. nuevo formato de `tasks.json`).

---

### 1.3.0 — Publicada

**Alcance**

- Proyecto y paquete renombrados a `tasks-cli` / `tasks_cli` (antes `task-cli` / `task_cli`).
- Comando de ejecución: `python -m tasks_cli`.

---

### 1.2.0 — Publicada

**Alcance**

- Suite de pruebas en `tests/` con `unittest` (solo librería estándar).
- `test_tasks.py`: agregar, completar, editar, buscar y eliminar tareas.
- `test_storage.py`: carga y guardado con archivos temporales aislados.

---

### 1.1.0 — Publicada

**Alcance**

- Editar el título de una tarea existente por `id` (opción 5 del menú).
- Buscar tareas cuyo título contenga un texto dado, sin distinguir mayúsculas/minúsculas (opción 6).
- Salir pasa a la opción 7 del menú.

**Comportamiento de guardado**

| Operación                   | Guarda |
|-----------------------------|--------|
| Editar título (cambio real) | Sí     |
| Editar con mismo título     | No     |
| Editar `id` inexistente     | No     |
| Editar con título inválido  | No     |
| Buscar por texto            | No     |

**Fuera de alcance en 1.1.0**

- Cambiar el modelo JSON (`id`, `title`, `completed` se mantienen).
- Editar `completed` desde la opción de edición (sigue siendo la opción de completar).
- Búsqueda por `id`, por estado completado o por campos que no existan.
- Pruebas automatizadas (incorporadas en `1.2.0`).

---

### 1.0.0 — Publicada

**Alcance**

- Menú interactivo por consola.
- Agregar tareas (título obligatorio, sin espacios vacíos).
- Listar todas las tareas con su estado de completado.
- Marcar una tarea pendiente como completada.
- Eliminar una tarea por `id`.
- Cargar tareas desde `tasks.json` al iniciar.
- Guardar en `tasks.json` solo cuando una operación modifica datos realmente.

**Comportamiento de guardado**

| Operación                         | Guarda |
|-----------------------------------|--------|
| Agregar tarea válida              | Sí     |
| Listar tareas                     | No     |
| Completar tarea pendiente         | Sí     |
| Completar tarea ya completada     | No     |
| Completar `id` inexistente        | No     |
| Eliminar tarea existente          | Sí     |
| Eliminar `id` inexistente         | No     |

**Fuera de alcance en 1.0.0**

- Editar el título de una tarea.
- Buscar o filtrar tareas.
- Prioridades, fechas, etiquetas u otros campos.

---

## Reglas del proyecto

Convenciones de código, guardado y estructura: ver `.cursor/rules/project.mdc`.
