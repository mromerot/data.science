---
title: Introducción a VS Code
short_title: 1. Introducción
subtitle: Qué es, cómo instalarlo y cómo moverse por la interfaz
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Al terminar esta página podrá instalar VS Code, reconocer las partes de su interfaz, abrir un proyecto y usar la **Paleta de comandos**, la herramienta que da acceso a todas sus funciones.
:::

## ¿Qué es Visual Studio Code?

Visual Studio Code (VS Code) es un editor de código fuente gratuito y de código abierto desarrollado por Microsoft. Es liviano pero muy potente, funciona en Windows, macOS y Linux, y se ha convertido en el editor más usado por desarrolladores de software según encuestas anuales como la de Stack Overflow.

Sus características principales incluyen resaltado de sintaxis para prácticamente cualquier lenguaje, autocompletado inteligente (IntelliSense), depuración integrada, control de versiones con Git incorporado, una terminal integrada y un enorme ecosistema de extensiones que permiten adaptarlo a cualquier flujo de trabajo, desde ciencia de datos hasta desarrollo web o escritura de documentos.

:::{iframe} https://www.youtube.com/embed/f8_uF_IDV50
:width: 100%
Learn Visual Studio Code in 15 minutes: 2026 Official Beginner Tutorial (canal oficial de VS Code).
:::

:::{note} VS Code no es Visual Studio
**Visual Studio** es un entorno de desarrollo completo (IDE), sobre todo para .NET y C++ en Windows. **VS Code** es un editor ligero y multiplataforma que se vuelve un entorno completo a medida que le añade extensiones. Su núcleo abierto (*Code - OSS*) es la base de otros editores, como VSCodium o Positron, el entorno de Posit para ciencia de datos con R y Python.
:::

## Instalación

Descargue el instalador desde <https://code.visualstudio.com/> y siga los pasos de su sistema:

| Sistema | Cómo instalar | Detalle importante |
| --- | --- | --- |
| Windows | Instalador *User Installer* (`.exe`) | Deje marcadas las opciones **Add to PATH** y **Add "Open with Code" action**, que permiten abrir carpetas desde el explorador y desde la terminal. |
| macOS | Archivo `.zip`: arrastre la aplicación a *Aplicaciones* | Para usar el comando `code` en la terminal, abra la Paleta de comandos y ejecute **Shell Command: Install 'code' command in PATH**. |
| Linux | Paquete `.deb` (Debian, Ubuntu) o `.rpm` (Fedora, RHEL), o Snap | El paquete agrega el repositorio de Microsoft para recibir actualizaciones. |

Compruebe la instalación desde una terminal:

```bash
code --version
```

:::{tip} VS Code en español
La interfaz viene en inglés. Para cambiarla, abra la Paleta de comandos, ejecute **Configure Display Language** y elija *Español*, que instala el paquete de idioma. Esta guía nombra los comandos en inglés, como aparecen por defecto; con el paquete en español, la Paleta de comandos muestra la traducción y sigue encontrando los comandos por su nombre en inglés.
:::

## La interfaz

La ventana de VS Code se organiza siempre de la misma manera:

| Zona | Dónde está | Para qué sirve |
| --- | --- | --- |
| **Barra de actividades** (*Activity Bar*) | Columna de íconos a la izquierda | Cambia entre las vistas principales: Explorador, Búsqueda, Control de código fuente, Ejecutar y depurar, Extensiones. |
| **Barra lateral** (*Primary Side Bar*) | Junto a la barra de actividades | Muestra la vista elegida, por ejemplo el árbol de archivos del proyecto. |
| **Editor** | Centro | Donde se escriben los archivos. Admite pestañas y dividirse en varios grupos lado a lado. |
| **Panel** | Debajo del editor | Terminal, Problemas, Salida y Consola de depuración. |
| **Barra de estado** (*Status Bar*) | Franja inferior | Rama de Git, errores y advertencias, lenguaje del archivo, intérprete de Python, codificación y fin de línea. |
| **Barra lateral secundaria** | Derecha | Espacio opcional; suele alojar el chat de los asistentes de IA. |

Dos atajos ocultan y muestran zonas para ganar espacio: `Ctrl+B` (`Cmd+B` en macOS) para la barra lateral y `Ctrl+J` (`Cmd+J`) para el panel.

## Trabajar con carpetas, no con archivos sueltos

VS Code está pensado para abrir **una carpeta de proyecto** (*File → Open Folder…*), no archivos aislados. Al abrir una carpeta, el editor la trata como su *espacio de trabajo* (*workspace*): el Explorador muestra sus archivos, la búsqueda recorre todo el proyecto, Git detecta el repositorio y la configuración propia del proyecto se guarda en una subcarpeta `.vscode/`.

Desde una terminal, el comando `code` abre la carpeta actual:

```bash
cd ~/proyectos/mi-analisis
code .
```

La primera vez que abre una carpeta, VS Code pregunta si confía en sus autores (**Workspace Trust**). Si responde que no, se abre en *modo restringido*: puede leer y editar, pero no se ejecutan tareas, depuradores ni extensiones que puedan correr código del proyecto. Es una protección útil cuando descarga repositorios de origen desconocido.

## La Paleta de comandos

Todo lo que VS Code sabe hacer está en la **Paleta de comandos**: `Ctrl+Shift+P` (`Cmd+Shift+P` en macOS) o `F1`. Escriba parte del nombre del comando, por ejemplo `toggle terminal` o `format`, y presione `Enter`. Junto a cada comando aparece su atajo de teclado, así que la paleta también sirve para aprenderlos.

La misma caja cambia de función según el primer carácter:

| Escriba | Abre con | Resultado |
| --- | --- | --- |
| (nada) | `Ctrl+P` / `Cmd+P` | **Quick Open**: buscar y abrir archivos del proyecto por nombre. |
| `>` | `Ctrl+Shift+P` / `Cmd+Shift+P` | Ejecutar un comando. |
| `@` | `Ctrl+Shift+O` / `Cmd+Shift+O` | Saltar a una función, clase o encabezado del archivo actual. |
| `:` | `Ctrl+G` | Ir a un número de línea. |
| `?` | — | Ver todas las opciones disponibles. |

:::{tip} El atajo más importante
Si solo recuerda un atajo, que sea `Ctrl+Shift+P`. Cualquier función que no encuentre en los menús está en la Paleta de comandos.
:::

## La terminal integrada

Con `` Ctrl+` `` (la tecla del acento grave, también en macOS) se abre una terminal dentro del editor, ubicada en la carpeta del proyecto. Puede tener varias a la vez (`` Ctrl+Shift+` `` crea una nueva), elegir el intérprete de comandos (PowerShell, bash, zsh) desde el menú desplegable del panel y dividirlas lado a lado. Los errores que imprimen muchos programas incluyen rutas de archivo: con `Ctrl+clic` sobre ellas se abre el archivo en la línea indicada.

## Ruta de aprendizaje de esta sección

| Página | Nivel | Qué aprenderá |
| --- | --- | --- |
| [1. Introducción](01-vscode.md) | Básico | Instalación, interfaz, carpetas, Paleta de comandos y terminal. |
| [2. Edición e IntelliSense](02-edicion.md) | Básico | Atajos esenciales, autocompletado, multicursor, búsqueda con expresiones regulares y navegación por el código. |
| [3. Extensiones y configuración](03-extensiones-configuracion.md) | Básico–intermedio | Extensiones para ciencia de datos, `settings.json`, configuración por proyecto y perfiles. |
| [4. Python y Jupyter](04-python-jupyter.md) | Intermedio | Intérpretes y entornos virtuales, notebooks, ventana interactiva y calidad de código. |
| [5. Depuración](05-depuracion.md) | Intermedio | Puntos de interrupción, inspección de variables y `launch.json`. |
| [6. Git y GitHub](06-git.md) | Intermedio | Commits, ramas, conflictos y publicación en GitHub sin salir del editor. |
| [7. Escritura y documentación](07-escritura.md) | Básico–intermedio | VS Code para no desarrolladores: Markdown, MyST, Quarto y corrección ortográfica. |
| [8. Productividad intermedia](08-productividad.md) | Intermedio | Fragmentos, tareas, desarrollo remoto, contenedores y asistentes de IA. |

## Práctica

1. Instale VS Code y, si lo prefiere, el paquete de idioma en español.
2. Cree una carpeta `practica-vscode`, ábrala con *File → Open Folder…* y cree un archivo `notas.md` desde el Explorador.
3. Con la Paleta de comandos, ejecute **View: Toggle Minimap** y luego **View: Toggle Zen Mode**. Salga del modo Zen con `Esc Esc`.
4. Abra la terminal integrada y escriba `code --version`.
