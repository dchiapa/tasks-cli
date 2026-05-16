# task-cli

Aplicación de consola en Python para gestionar tareas simples. Usa solo la librería estándar y persiste los datos en `tasks.json` en la raíz del proyecto.

## Versión actual

`1.0.0` — definida en `task_cli.__version__`.

## Requisitos

- Python 3.10 o superior

## Ejecución

Desde la raíz del proyecto:

```bash
python -m task_cli
```

## Estructura

```text
task-cli/
├── .cursor/
│   └── rules/
│       └── project.mdc
├── task_cli/              # Código de la aplicación
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
| `1.1.0`   | Planificada | Editar título y buscar tareas por texto      |

> La “v2” del plan funcional corresponde a **`1.1.0`**: agrega capacidades sin romper el modelo de datos ni el formato de `tasks.json`. Un **`2.0.0`** se reservaría para cambios incompatibles.

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

### 1.1.0 — Planificada

**Objetivo**

Ampliar el menú con edición de títulos y búsqueda por texto, sin cambiar el modelo de datos ni las dependencias del proyecto.

**Alcance propuesto**

1. **Editar título**
   - Nueva opción en el menú: elegir una tarea por `id` e ingresar un título nuevo.
   - Validar igual que al agregar: no permitir título vacío ni solo espacios.
   - Si el `id` no existe, informar y no modificar datos.
   - Si el título nuevo es igual al actual (tras normalizar espacios al inicio/fin), informar que no hubo cambios y **no guardar**.
   - Si el título cambia, actualizar la tarea y **guardar** `tasks.json`.

2. **Buscar por texto en el título**
   - Nueva opción en el menú: ingresar un texto de búsqueda.
   - Mostrar las tareas cuyo `title` contenga ese texto (comparación sin distinguir mayúsculas/minúsculas).
   - Si no hay coincidencias, informarlo claramente.
   - **No modificar** la lista ni **guardar** el archivo.

**Reglas de comportamiento (1.1.0)**

| Operación              | Modifica datos | Guarda |
|------------------------|----------------|--------|
| Editar título (cambio real) | Sí        | Sí     |
| Editar con mismo título     | No        | No     |
| Editar `id` inexistente     | No        | No     |
| Editar con título inválido  | No        | No     |
| Buscar por texto            | No        | No     |

**Fuera de alcance en 1.1.0**

- Cambiar el modelo JSON (`id`, `title`, `completed` se mantienen).
- Editar `completed` desde la opción de edición (sigue siendo la opción de completar).
- Búsqueda por `id`, por estado completado o por campos que no existan.
- Dependencias externas, API HTTP, interfaz gráfica o tests automatizados (salvo que se pidan explícitamente).

**Archivos previstos a tocar en la implementación**

- `task_cli/tasks.py` — funciones `edit_task` y `search_tasks` (o equivalentes).
- `task_cli/cli.py` — nuevas opciones de menú, mensajes y llamadas a guardado.
- `README.md` — actualizar el estado de `1.1.0` a *publicada* y el historial de releases al cerrar la versión.

---

## Reglas del proyecto

Convenciones de código, guardado y estructura: ver `.cursor/rules/project.mdc`.
