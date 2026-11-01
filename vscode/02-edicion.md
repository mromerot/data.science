---
title: Edición de código e IntelliSense
short_title: 2. Edición e IntelliSense
subtitle: Escribir, buscar y navegar el código con rapidez
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Usar el autocompletado, editar varias líneas a la vez, buscar y reemplazar con expresiones regulares en todo el proyecto y moverse entre definiciones y referencias sin perder el hilo.
:::

## El editor e IntelliSense

El corazón de VS Code es su editor de texto, diseñado para que escribir y navegar código sea rápido y cómodo. Incluye **IntelliSense**, un motor de autocompletado que sugiere variables, funciones y métodos según el lenguaje, además de mostrar información de tipos y documentación en línea mientras se escribe.

Otras características de edición destacadas son el resaltado de sintaxis, el plegado de código (*code folding*), la búsqueda y reemplazo con expresiones regulares, la edición multicursor, y la navegación rápida a definiciones y referencias (*Go to Definition* / *Find All References*), lo que agiliza el trabajo en proyectos grandes.

:::{iframe} https://www.youtube.com/embed/MNBwGGwvvKE
:width: 100%
Edit and Run Code in Visual Studio Code (canal oficial de VS Code).
:::

IntelliSense depende del lenguaje: para Python lo aporta la extensión de Python (con Pylance), para R la extensión de R, y para JavaScript, HTML, CSS, JSON y Markdown viene incluido. Cuando escribe, aparece una lista de sugerencias; las flechas la recorren, `Tab` o `Enter` aceptan y `Esc` la cierra. Si la lista no aparece, `Ctrl+Space` la fuerza. Al abrir el paréntesis de una función, VS Code muestra sus parámetros (`Ctrl+Shift+Space` para volver a verlos) y, al pasar el ratón sobre un nombre, su documentación.

## Atajos esenciales

No hace falta memorizarlos todos de una vez: aprenda dos o tres por semana. Los de esta tabla cubren la mayor parte del trabajo diario.

| Acción | Windows / Linux | macOS |
| --- | --- | --- |
| Paleta de comandos | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Abrir archivo por nombre | `Ctrl+P` | `Cmd+P` |
| Guardar | `Ctrl+S` | `Cmd+S` |
| Comentar o descomentar líneas | `Ctrl+/` | `Cmd+/` |
| Mover la línea arriba o abajo | `Alt+↑` / `Alt+↓` | `Option+↑` / `Option+↓` |
| Borrar la línea | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| Insertar línea debajo (sin partir la actual) | `Ctrl+Enter` | `Cmd+Enter` |
| Seleccionar la línea | `Ctrl+L` | `Cmd+L` |
| Ajuste de línea (*word wrap*) | `Alt+Z` | `Option+Z` |
| Dividir el editor | `Ctrl+\` | `Cmd+\` |
| Cerrar la pestaña | `Ctrl+W` | `Cmd+W` |
| Mostrar u ocultar la terminal | `` Ctrl+` `` | `` Ctrl+` `` |
| Ver todos los atajos | `Ctrl+K Ctrl+S` | `Cmd+K Cmd+S` |

`Ctrl+K Ctrl+S` significa: presione `Ctrl+K`, suelte, y luego `Ctrl+S`. VS Code usa muchas de estas *combinaciones encadenadas*.

## Edición multicursor

Con varios cursores puede escribir lo mismo en muchos lugares a la vez, una de las funciones que más tiempo ahorra.

| Acción | Windows / Linux | macOS |
| --- | --- | --- |
| Agregar un cursor donde haga clic | `Alt+clic` | `Option+clic` |
| Agregar cursor arriba o abajo | `Ctrl+Alt+↑/↓` (Windows), `Shift+Alt+↑/↓` (Linux) | `Cmd+Option+↑/↓` |
| Seleccionar la siguiente aparición de la selección | `Ctrl+D` | `Cmd+D` |
| Seleccionar todas las apariciones | `Ctrl+Shift+L` | `Cmd+Shift+L` |
| Deshacer el último cursor | `Ctrl+U` | `Cmd+U` |
| Selección en columna (bloque) | `Shift+Alt` + arrastrar | `Shift+Option` + arrastrar |

**Ejemplo.** Tiene una lista de nombres de columnas y quiere convertirla en una lista de Python:

```text
temperatura
precipitacion
humedad
```

Seleccione las tres líneas, presione `Shift+Alt+I` (`Shift+Option+I` en macOS) para poner un cursor al final de cada una, escriba `",`, luego `Home` para ir al inicio y escriba `"`. El resultado es:

```text
"temperatura",
"precipitacion",
"humedad",
```

## Buscar y reemplazar

`Ctrl+F` busca en el archivo y `Ctrl+H` reemplaza (`Cmd+F` y `Cmd+Option+F` en macOS). `Ctrl+Shift+F` (`Cmd+Shift+F`) busca en **todo el proyecto**, con filtros de archivos a incluir o excluir, por ejemplo `*.md` o `datos/**`.

Los tres botones de la caja de búsqueda activan opciones: `Aa` distingue mayúsculas, `ab` busca palabras completas y `.*` activa **expresiones regulares**. En el reemplazo, `$1`, `$2`… insertan los grupos capturados con paréntesis.

**Ejemplo.** Convertir fechas `31/12/2024` al formato ISO `2024-12-31`:

| Campo | Valor |
| --- | --- |
| Buscar | `(\d{2})/(\d{2})/(\d{4})` |
| Reemplazar | `$3-$2-$1` |

:::{warning} Revise antes de reemplazar en todo el proyecto
El reemplazo global (`Ctrl+Shift+H`) muestra una vista previa de cada cambio. Revísela, y si el proyecto está en Git, haga un commit antes: así podrá deshacer el reemplazo completo si algo sale mal.
:::

## Navegar por el código

En proyectos con muchos archivos, saltar entre definiciones y usos es más rápido que buscar a mano.

| Acción | Atajo | Para qué |
| --- | --- | --- |
| Ir a la definición | `F12` o `Ctrl+clic` (`Cmd+clic`) | Abre el lugar donde se definió la función o variable. |
| Ver la definición sin salir (*Peek*) | `Alt+F12` (`Option+F12`) | La muestra en una ventana incrustada. |
| Ver todas las referencias | `Shift+F12` | Lista los lugares donde se usa. |
| Renombrar símbolo | `F2` | Cambia el nombre en todos los usos, no solo en el texto que coincide. |
| Volver a la posición anterior | `Alt+←` (Windows), `Ctrl+Alt+-` (Linux), `Ctrl+-` (macOS) | Regresa después de un salto. |
| Ir a un símbolo del archivo | `Ctrl+Shift+O` (`Cmd+Shift+O`) | Funciones, clases o encabezados de Markdown. |
| Ir a un símbolo del proyecto | `Ctrl+T` (`Cmd+T`) | Busca en todos los archivos. |

Las **migas de pan** (*breadcrumbs*), sobre el editor, muestran la ruta del archivo y la función en la que está el cursor; al hacer clic en ellas puede saltar a otra función del mismo archivo.

## Plegado, formato y problemas

- **Plegado.** Las flechas del margen pliegan bloques de código. `Ctrl+K Ctrl+0` pliega todo y `Ctrl+K Ctrl+J` lo despliega. En Python puede crear regiones plegables propias con comentarios `# region Nombre` y `# endregion`.
- **Formato.** *Format Document* (`Shift+Alt+F` en Windows, `Ctrl+Shift+I` en Linux, `Shift+Option+F` en macOS) ordena sangrías y espacios con el formateador del lenguaje. En la [página 3](03-extensiones-configuracion.md) verá cómo aplicarlo al guardar.
- **Problemas.** Los errores y advertencias se subrayan en el código y se reúnen en el panel *Problems* (`Ctrl+Shift+M`). Sobre un subrayado, `Ctrl+.` (`Cmd+.`) ofrece **correcciones rápidas** (*Quick Fix*), como agregar un `import` que falta.

## Práctica

1. Copie en un archivo `columnas.txt` unos diez nombres de columnas, uno por línea, y conviértalos en una lista de Python con multicursor.
2. Escriba en un archivo varias fechas `dd/mm/aaaa` y páselas a `aaaa-mm-dd` con una expresión regular.
3. En un archivo `.py`, defina una función `celsius_a_fahrenheit` y úsela en tres lugares. Renómbrela con `F2` a `c_a_f` y compruebe que cambian todos los usos.
