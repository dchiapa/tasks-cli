# task-cli

Aplicación de consola en Python para gestionar tareas simples. Usa solo la librería estándar y persiste los datos en `tasks.json` en la raíz del proyecto.

## Versión actual

`1.2.0` — definida en `task_cli.__version__`.

## Requisitos

- Python 3.10 o superior

## Ejecución

Desde la raíz del proyecto:

```bash
python -m task_cli
```

## Pruebas

Desde la raíz del proyecto (solo librería estándar, `unittest`):

```bash
python -m unittest discover -s tests -v
```

## Estructura

```text
task-cli/
├── .cursor/
│   └── rules/
│       └── project.mdc
├── task_cli/              # Código de la aplicación
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

| Componente | Cuándo incrementarlo en task-cli                          |
|------------|-----------------------------------------------------------|
| **MAYOR**  | Cambios incompatibles (p. ej. nuevo formato de `tasks.json`) |
| **MENOR**  | Funcionalidad nueva compatible con versiones anteriores   |
| **PARCHE** | Correcciones de bugs sin cambiar el comportamiento esperado |

Estado de cada release: **publicada** (disponible) o **planificada** (definida, sin implementar).

| Versión   | Estado      | Resumen                                      |
|-----------|-------------|----------------------------------------------|
| `1.0.0`   | Publicada   | CRUD básico, menú por consola, persistencia  |
| `1.1.0`   | Publicada   | Editar título y buscar tareas por texto      |
| `1.2.0`   | Publicada   | Suite de pruebas automatizadas (`unittest`)  |

> Un **`2.0.0`** se reservaría para cambios incompatibles (p. ej. nuevo formato de `tasks.json`).

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

### 1.2.0 — Publicada

**Alcance**

- Suite de pruebas en `tests/` con `unittest` (solo librería estándar).
- `test_tasks.py`: agregar, completar, editar, buscar y eliminar tareas.
- `test_storage.py`: carga y guardado con archivos temporales aislados.

---

## Reglas del proyecto

Convenciones de código, guardado y estructura: ver `.cursor/rules/project.mdc`.
