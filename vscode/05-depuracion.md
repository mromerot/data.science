---
title: Depuración de código
short_title: 5. Depuración
subtitle: Encontrar errores observando el programa mientras se ejecuta
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Detener un programa en el punto exacto que interesa, inspeccionar sus variables, avanzar línea a línea, usar puntos de interrupción condicionales y guardar configuraciones de depuración en `launch.json`.
:::

## El depurador integrado

VS Code incluye un depurador (*debugger*) integrado que permite ejecutar el código paso a paso, inspeccionar variables, establecer puntos de interrupción (*breakpoints*) y evaluar expresiones en tiempo real, sin necesidad de salir del editor.

Esta funcionalidad es compatible de forma nativa con Node.js y, mediante extensiones, con la mayoría de los lenguajes populares como Python, Java, C++ o Go. La configuración de depuración se guarda en un archivo `launch.json`, lo que facilita reutilizar y compartir configuraciones entre miembros de un equipo.

:::{iframe} https://www.youtube.com/embed/3HiLLByBWkg
:width: 100%
Getting Started with Debugging in VS Code (Official Beginner Guide), canal oficial de VS Code.
:::

Llenar el código de `print()` funciona, pero obliga a adivinar qué imprimir y a volver a ejecutar cada vez. El depurador detiene el programa y deja ver **todo** su estado en ese instante.

## Un error para practicar

Guarde este script como `promedios.py`. Calcula la temperatura media diaria de una estación, pero uno de los registros no tiene dato:

```python
def promedio_diario(registros):
    """Temperatura media por día a partir de una lista de registros."""
    sumas, conteos = {}, {}
    for r in registros:
        dia = r["fecha"][:10]
        sumas[dia] = sumas.get(dia, 0) + r["temp"]
        conteos[dia] = conteos.get(dia, 0) + 1
    return {dia: sumas[dia] / conteos[dia] for dia in sumas}


registros = [
    {"fecha": "2024-03-01 06:00", "temp": 12.5},
    {"fecha": "2024-03-01 12:00", "temp": 21.0},
    {"fecha": "2024-03-02 06:00", "temp": None},  # el sensor no reportó
    {"fecha": "2024-03-02 12:00", "temp": 19.5},
]
print(promedio_diario(registros))
```

Al ejecutarlo, Python se detiene con `TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'`. En un archivo con miles de registros, encontrar cuál falla a punta de `print()` es tedioso. Veamos cómo hacerlo con el depurador.

## Depurar paso a paso

1. **Ponga un punto de interrupción.** Haga clic en el margen izquierdo de la línea `sumas[dia] = ...` (o ubique el cursor y presione `F9`). Aparece un punto rojo.
2. **Inicie la depuración** con `F5` y elija *Python Debugger → Python File*. El programa se detiene en la línea marcada, antes de ejecutarla, y VS Code cambia a la vista **Run and Debug**.
3. **Inspeccione.** La sección *Variables* muestra `r`, `dia`, `sumas` y `conteos` con sus valores. Al pasar el ratón sobre una variable del código también se ve su valor.
4. **Avance** con la barra flotante de depuración:

| Botón | Atajo | Qué hace |
| --- | --- | --- |
| Continuar | `F5` | Sigue hasta el siguiente punto de interrupción. |
| Saltar (*Step Over*) | `F10` | Ejecuta la línea actual completa y se detiene en la siguiente. |
| Entrar (*Step Into*) | `F11` | Si la línea llama a una función, entra en ella. |
| Salir (*Step Out*) | `Shift+F11` | Termina la función actual y vuelve a quien la llamó. |
| Reiniciar | `Ctrl+Shift+F5` (`Cmd+Shift+F5`) | Vuelve a empezar. |
| Detener | `Shift+F5` | Termina la sesión de depuración. |

Presione `F5` varias veces: en cada vuelta del ciclo, `r` cambia. En la tercera verá `r = {'fecha': '2024-03-02 06:00', 'temp': None}`, el registro culpable.

## Las vistas del depurador

| Vista | Para qué sirve |
| --- | --- |
| **Variables** | Variables locales y globales en el punto de parada. Doble clic sobre un valor para cambiarlo y probar una hipótesis sin reiniciar. |
| **Watch** | Expresiones que quiere vigilar, por ejemplo `len(sumas)` o `r["temp"] is None`. Se recalculan en cada paso. |
| **Call Stack** | La cadena de llamadas que llevó hasta la línea actual. Haga clic en un nivel para ver las variables de esa función. |
| **Breakpoints** | Lista de puntos de interrupción, que puede desactivar sin borrarlos. Incluye casillas para detenerse ante excepciones (*Raised Exceptions*, *Uncaught Exceptions*). |
| **Debug Console** | Una consola en el contexto del programa detenido. Escriba `r`, `sumas` o `[x["temp"] for x in registros]` y vea el resultado. |

## Puntos de interrupción avanzados

Haga clic derecho en el margen y elija **Add Conditional Breakpoint** para obtener tres variantes:

- **Expresión.** Se detiene solo si la condición es verdadera. Con `r["temp"] is None` en el ejemplo, el programa se detiene directamente en el registro defectuoso, aunque sea el número 50 000.
- **Conteo de pasadas** (*Hit Count*). Se detiene a partir de la enésima vez que pasa por la línea, útil en ciclos largos.
- **Punto de registro** (*Logpoint*). No detiene nada: escribe un mensaje en la Debug Console, como un `print()` que no hay que agregar ni borrar del código. Las expresiones van entre llaves: `día {dia}, temperatura {r["temp"]}`.

Una vez encontrado el problema, corrija el código para ignorar los registros sin dato:

```python
    for r in registros:
        if r["temp"] is None:
            continue
        dia = r["fecha"][:10]
```

## Configuraciones reutilizables: `launch.json`

Para scripts que reciben argumentos, variables de entorno o se ejecutan desde otra carpeta, conviene guardar la configuración. En la vista **Run and Debug**, haga clic en *create a launch.json file* y elija *Python Debugger*. VS Code crea `.vscode/launch.json`, que puede editar:

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: archivo actual",
      "type": "debugpy",
      "request": "launch",
      "program": "${file}",
      "console": "integratedTerminal"
    },
    {
      "name": "Procesar estaciones 2024",
      "type": "debugpy",
      "request": "launch",
      "program": "${workspaceFolder}/src/procesar.py",
      "args": ["--anio", "2024", "--entrada", "datos/estaciones.csv"],
      "cwd": "${workspaceFolder}",
      "env": { "NIVEL_LOG": "DEBUG" },
      "justMyCode": false
    }
  ]
}
```

- `${file}` es el archivo abierto y `${workspaceFolder}` la carpeta del proyecto.
- `args` equivale a escribir los argumentos en la terminal: `python src/procesar.py --anio 2024 ...`.
- `"justMyCode": false` permite entrar con `F11` en el código de las librerías, por ejemplo para entender qué hace pandas con sus datos.

Las configuraciones aparecen en el menú desplegable de la vista *Run and Debug*; `F5` lanza la que esté seleccionada. Si versiona `.vscode/launch.json` en Git, todo el equipo depura igual.

## Depurar notebooks

En un notebook de Jupyter hay dos opciones en la barra de cada celda: **Run by Line**, que ejecuta la celda una línea a la vez mostrando las variables, y **Debug Cell** (en el menú desplegable junto al botón ▷), que respeta los puntos de interrupción puestos en la celda y abre todas las vistas del depurador.

## Práctica

1. Reproduzca el error de `promedios.py` y encuentre el registro defectuoso con un punto de interrupción condicional.
2. Agregue un *logpoint* que imprima el día y la temperatura de cada registro y compare con un `print()`.
3. En la Debug Console, calcule `sum(1 for x in registros if x["temp"] is None)` mientras el programa está detenido.
4. Cree un `launch.json` con una configuración que pase un argumento a un script de prueba que lo lea con `sys.argv`.
