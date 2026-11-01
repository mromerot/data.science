---
title: Productividad intermedia
short_title: 8. Productividad intermedia
subtitle: Fragmentos, tareas, desarrollo remoto, contenedores y asistentes de IA
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Automatizar lo repetitivo con fragmentos y tareas, trabajar en varios proyectos a la vez, programar en servidores y contenedores como si fueran locales y usar asistentes de IA con criterio.
:::

## Fragmentos de código (*snippets*)

Un fragmento es una plantilla que se inserta al escribir un prefijo. VS Code trae muchos para cada lenguaje, y puede crear los suyos con **Snippets: Configure Snippets**, eligiendo un lenguaje (por ejemplo `markdown`) o un archivo de fragmentos del proyecto.

Este fragmento inserta una admonición de MyST al escribir `nota`:

```json
{
  "Nota de MyST": {
    "prefix": "nota",
    "body": [
      ":::{${1|note,tip,warning,important|}} ${2:Título}",
      "$0",
      ":::"
    ],
    "description": "Admonición de MyST"
  }
}
```

- `$1`, `$2`… son los puntos por los que se salta con `Tab`; `$0` es donde queda el cursor al final.
- `${2:Título}` es un punto con texto por defecto.
- `${1|note,tip,warning,important|}` ofrece una lista para elegir.

En Markdown las sugerencias automáticas vienen desactivadas: escriba `nota` y presione `Ctrl+Space` para ver el fragmento.

## Tareas: automatizar comandos

Las **tareas** guardan comandos de terminal que repite a menudo (compilar, probar, generar un informe) y los ejecutan con **Tasks: Run Task**. Se definen en `.vscode/tasks.json`. Para un proyecto de MyST como este libro:

```json
{
  "version": "2.0.0",
  "tasks": [
    {
      "label": "MyST: vista previa",
      "type": "shell",
      "command": "myst start",
      "isBackground": true,
      "problemMatcher": []
    },
    {
      "label": "MyST: construir HTML",
      "type": "shell",
      "command": "myst build --html",
      "group": { "kind": "build", "isDefault": true },
      "problemMatcher": []
    }
  ]
}
```

La tarea marcada como `"isDefault": true` en el grupo `build` se ejecuta directamente con `Ctrl+Shift+B` (`Cmd+Shift+B` en macOS). Al estar en el repositorio, cualquier colaborador tiene los mismos comandos a un clic.

## Varios proyectos en una ventana

Un **espacio de trabajo multirraíz** reúne varias carpetas en la misma ventana, por ejemplo los datos, el análisis y el libro que lo publica. Agregue carpetas con *File → Add Folder to Workspace…* y guarde el conjunto con *File → Save Workspace As…*, que crea un archivo `.code-workspace`:

```json
{
  "folders": [
    { "path": "analisis-lluvias" },
    { "path": "data.science" }
  ],
  "settings": {
    "files.autoSave": "afterDelay"
  }
}
```

Al abrir ese archivo se recupera todo el conjunto. La búsqueda, Git y la depuración funcionan en todas las carpetas.

## Desarrollo remoto

VS Code puede ejecutar su parte pesada (terminal, extensiones, depurador) en otra máquina mientras usted trabaja con la interfaz local de siempre. Es la forma cómoda de usar un servidor con GPU o los datos de un clúster sin copiarlos.

| Extensión o servicio | Dónde corre el código | Cuándo usarlo |
| --- | --- | --- |
| **Remote - SSH** (`ms-vscode-remote.remote-ssh`) | Un servidor al que tiene acceso por SSH | Servidores de la universidad o de la nube, máquinas con GPU. |
| **WSL** (`ms-vscode-remote.remote-wsl`) | El subsistema de Linux de Windows | Herramientas que funcionan mejor en Linux, desde un PC con Windows. |
| **Dev Containers** (`ms-vscode-remote.remote-containers`) | Un contenedor de Docker | Entornos reproducibles e idénticos para todo un equipo. |
| **GitHub Codespaces** | Un contenedor en la nube de GitHub | Trabajar desde cualquier computador o desde el navegador. |

Todas se manejan desde el indicador remoto (el ícono `><`) de la esquina inferior izquierda de la barra de estado.

### Un entorno reproducible con Dev Containers

Un archivo `.devcontainer/devcontainer.json` describe el entorno del proyecto. Con Docker instalado, el comando **Dev Containers: Reopen in Container** lo construye y abre el proyecto dentro:

```json
{
  "name": "ciencia-de-datos",
  "image": "mcr.microsoft.com/devcontainers/python:3.12",
  "postCreateCommand": "pip install -r requirements.txt",
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python", "ms-toolsai.jupyter"]
    }
  }
}
```

Cualquier persona que abra el repositorio obtiene la misma versión de Python, los mismos paquetes y las mismas extensiones; el mismo archivo sirve para GitHub Codespaces. Es un paso concreto hacia la ciencia reproducible.

## Asistentes de IA

VS Code integra asistentes de IA que completan código mientras se escribe, responden preguntas sobre el proyecto en un panel de chat y, en modo agente, pueden editar varios archivos y ejecutar comandos en la terminal pidiendo permiso. **GitHub Copilot** viene integrado (con un plan gratuito limitado) y otros asistentes, como **Claude Code** (`anthropic.claude-code`), se instalan como extensiones.

Algunas recomendaciones para usarlos bien:

- **Revise todo lo que generan.** Funciones que parecen correctas pueden usar mal una librería, inventar parámetros o equivocarse en las unidades. Las pruebas y el depurador ([página 5](05-depuracion.md)) siguen siendo necesarios.
- **Pida cambios pequeños y verificables**, y haga un commit antes de aceptar ediciones grandes, para poder deshacerlas con Git.
- **Cuide los datos.** El contenido que envía al asistente sale de su computador. No comparta datos personales, credenciales ni información reservada sin revisar las políticas de su institución.
- **Úselos para aprender.** Pedir que expliquen un error, un comando de Git o una expresión regular es de sus usos más valiosos.

## La línea de comandos `code`

| Comando | Qué hace |
| --- | --- |
| `code .` | Abre la carpeta actual. |
| `code -g archivo.py:25` | Abre el archivo en la línea 25. |
| `code --diff a.csv b.csv` | Compara dos archivos. |
| `code --install-extension ID` | Instala una extensión. |
| `code --list-extensions > extensiones.txt` | Guarda la lista de extensiones instaladas. |
| `code -r .` | Abre la carpeta en la ventana ya abierta, sin crear otra. |

## Resumen y siguientes pasos

Con las ocho páginas de esta sección ya puede usar VS Code como entorno principal de ciencia de datos: editar con fluidez, configurar cada proyecto, trabajar con entornos de Python y notebooks, depurar, versionar con Git, escribir documentos y automatizar tareas. Para seguir avanzando:

- La documentación oficial, <https://code.visualstudio.com/docs>, tiene guías detalladas de cada tema.
- La hoja de atajos de su sistema: **Help → Keyboard Shortcuts Reference**.
- Las notas de cada versión (**Help → Show Release Notes**): VS Code se actualiza cada mes y casi siempre trae algo útil.

## Práctica

1. Cree el fragmento `nota` y úselo en un archivo Markdown.
2. Agregue a un proyecto un `tasks.json` con una tarea que ejecute un script de Python, y márquela como tarea de compilación por defecto.
3. Si tiene Docker, cree el `devcontainer.json` del ejemplo y abra el proyecto en el contenedor.
4. Pida a un asistente de IA que explique la expresión regular de la [página 2](02-edicion.md) y compruebe su explicación.
