---
title: Control de versiones con Git y GitHub
short_title: 6. Git y GitHub
subtitle: Commits, ramas y conflictos desde la interfaz del editor
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Clonar o iniciar un repositorio, preparar y confirmar cambios, trabajar con ramas, resolver conflictos de fusión y publicar en GitHub sin salir de VS Code, entendiendo qué comando de Git hay detrás de cada botón.
:::

## Git integrado

VS Code integra Git de forma nativa a través de la vista de **Control de código fuente** (*Source Control*), lo que permite ver los cambios realizados, hacer *stage* de archivos, crear commits, cambiar de rama, fusionar y resolver conflictos directamente desde la interfaz gráfica, sin depender exclusivamente de la línea de comandos.

También ofrece indicadores visuales en el margen del editor (*gutter*) que muestran líneas añadidas, modificadas o eliminadas respecto al último commit, y se integra con plataformas como GitHub para publicar (*push*), clonar repositorios y gestionar *pull requests* desde el mismo editor.

:::{iframe} https://www.youtube.com/embed/i_23KUAEtUM
:width: 100%
Using Git with Visual Studio Code (Official Beginner Tutorial), canal oficial de VS Code.
:::

## Antes de empezar

VS Code usa el Git instalado en el sistema; si no lo encuentra, la vista de control de código fuente ofrece descargarlo. La primera vez, configure su nombre y correo, que quedarán en cada commit:

```bash
git config --global user.name "Su Nombre"
git config --global user.email "su.correo@ejemplo.com"
```

## Obtener un repositorio

- **Clonar uno existente.** Ejecute **Git: Clone** en la Paleta de comandos, pegue la URL (por ejemplo `https://github.com/mromerot/data.science`) o elija *Clone from GitHub* para buscar entre sus repositorios, y escoja la carpeta de destino.
- **Convertir una carpeta en repositorio.** Con la carpeta abierta, en la vista *Source Control* (`Ctrl+Shift+G`), haga clic en **Initialize Repository** (equivale a `git init`).

## El ciclo básico: modificar, preparar, confirmar

La vista *Source Control* agrupa los archivos en **Changes** (modificados) y **Staged Changes** (preparados para el próximo commit). La letra junto a cada archivo indica su estado: `M` modificado, `U` nuevo sin seguimiento, `D` eliminado, `A` agregado.

| En VS Code | Comando de Git equivalente |
| --- | --- |
| Clic en un archivo de la lista | `git diff archivo`: abre la comparación lado a lado. |
| Botón **+** (*Stage Changes*) | `git add archivo` |
| Botón **−** (*Unstage Changes*) | `git restore --staged archivo` |
| Flecha curva (*Discard Changes*) | `git restore archivo`: **descarta** las modificaciones; no se puede deshacer. |
| Escribir el mensaje y **Commit** (o `Ctrl+Enter`) | `git commit -m "mensaje"` |
| **Sync Changes** o los botones de la barra de estado | `git pull` seguido de `git push` |

Si presiona *Commit* sin nada en *Staged Changes*, VS Code ofrece confirmar todos los cambios a la vez. El menú `···` de la vista reúne operaciones menos frecuentes: *Commit (Amend)* para corregir el último commit, *Stash* para guardar cambios temporalmente, *Pull (Rebase)* y otras.

:::{tip} Preparar solo una parte de un archivo
En la vista de comparación, seleccione unas líneas, haga clic derecho y elija **Stage Selected Ranges**. Así un mismo archivo puede repartirse en dos commits con propósitos distintos, por ejemplo «corrige cálculo» y «actualiza comentarios».
:::

### Indicadores en el editor

Mientras edita, el margen izquierdo marca en verde las líneas nuevas, en azul las modificadas y con un triángulo rojo las eliminadas. Al hacer clic en la marca se ve el cambio respecto al último commit y se puede revertir solo ese bloque.

## Ramas

La rama actual aparece en la esquina inferior izquierda de la barra de estado. Al hacer clic sobre ella puede cambiar de rama o crear una nueva (**Create new branch…**, equivalente a `git switch -c nombre`). La ventaja de trabajar en ramas es que `main` queda estable mientras prueba cambios.

Para incorporar una rama en la actual, use **Git: Merge…** en la Paleta de comandos. Una rama creada en su computador se sube a GitHub con **Publish Branch** (`git push -u origin nombre`).

La sección **Graph** de la vista *Source Control* dibuja el historial de commits y ramas, y la vista **Timeline** del Explorador muestra los commits que tocaron el archivo abierto.

## Resolver conflictos

Un conflicto ocurre cuando dos ramas modifican las mismas líneas. VS Code marca los archivos en conflicto con una `!` y, en el editor, muestra las dos versiones con botones encima:

- **Accept Current Change**: conservar la versión de su rama.
- **Accept Incoming Change**: conservar la versión que llega.
- **Accept Both Changes**: conservar ambas, una tras otra.
- **Compare Changes**: verlas lado a lado.

Para conflictos complejos, el botón **Resolve in Merge Editor** abre el **editor de fusión de tres vías**: arriba, las dos versiones en conflicto; abajo, el resultado, que puede construir marcando casillas o editando a mano. Cuando quede bien, *Complete Merge* prepara el archivo y solo falta el commit.

:::{warning} Lea antes de aceptar
Aceptar una versión entera sin leer la otra es la forma más común de perder trabajo ajeno. Revise siempre qué cambió en cada lado.
:::

## Trabajar con GitHub

- **Publicar un proyecto nuevo.** En un repositorio local sin remoto, el botón **Publish to GitHub** crea el repositorio en su cuenta (público o privado) y sube el contenido. VS Code pide autorizar el acceso a GitHub la primera vez.
- **Pull requests e issues.** La extensión **GitHub Pull Requests** (`GitHub.vscode-pull-request-github`) permite crear, revisar y comentar *pull requests* y ver los *issues* asignados desde el editor, con los comentarios de la revisión junto al código.
- **Editar sin instalar nada.** En cualquier repositorio de GitHub, presione la tecla `.` y se abre **github.dev**, una versión de VS Code en el navegador, ideal para corregir un texto rápido. Este libro, por ejemplo, se puede editar así.

## Un flujo de trabajo típico

1. Cree una rama para el cambio: `nueva-seccion-mapas`.
2. Edite y haga commits pequeños, cada uno con un mensaje que explique el porqué.
3. Publique la rama y abra un *pull request* en GitHub.
4. Revise los cambios, fusione en `main` y borre la rama.
5. Vuelva a `main` en VS Code y sincronice (*Sync Changes*).

## Práctica

1. Inicie un repositorio en `practica-vscode`, cree un `.gitignore` con `.venv/` y haga su primer commit.
2. Modifique dos partes distintas de un archivo y repártalas en dos commits con *Stage Selected Ranges*.
3. Cree la rama `prueba`, cambie una línea, vuelva a `main`, cambie la misma línea de otra forma y fusione `prueba`. Resuelva el conflicto en el editor de fusión.
4. Publique el repositorio en GitHub como privado.
