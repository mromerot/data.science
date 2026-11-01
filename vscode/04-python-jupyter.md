---
title: Python y Jupyter en VS Code
short_title: 4. Python y Jupyter
subtitle: Entornos virtuales, notebooks y ventana interactiva
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Elegir el intérprete de Python correcto, crear un entorno virtual por proyecto, trabajar con notebooks `.ipynb` y con scripts divididos en celdas, explorar *DataFrames* y mantener la calidad del código con un linter.
:::

## Preparación

Necesita Python instalado en el sistema (desde <https://www.python.org/> o con Anaconda/Miniconda) y dos extensiones: **Python** (`ms-python.python`) y **Jupyter** (`ms-toolsai.jupyter`). La primera instala automáticamente **Pylance**, que aporta el autocompletado y la revisión de tipos, y **Python Debugger**, que se usa en la [página 5](05-depuracion.md).

## El intérprete y los entornos virtuales

Un computador suele tener varios Pythons: el del sistema, uno de Anaconda, los de distintos proyectos. VS Code necesita saber cuál usar en cada carpeta. El intérprete activo aparece en la **barra de estado** cuando hay un archivo `.py` abierto; para cambiarlo, haga clic sobre él o ejecute **Python: Select Interpreter** en la Paleta de comandos.

La buena práctica es un **entorno virtual por proyecto**: una carpeta (por convención `.venv`) con su propio Python y sus propios paquetes, de modo que actualizar pandas en un proyecto no rompa otro.

**Desde VS Code.** Ejecute **Python: Create Environment**, elija *Venv* (o *Conda*), escoja la versión de Python y, si el proyecto tiene `requirements.txt`, marque la casilla para instalar sus paquetes. VS Code crea `.venv` y lo selecciona como intérprete. En versiones recientes, la extensión **Python Environments** agrega una vista propia en la barra de actividades para crear y administrar entornos; el resultado es el mismo.

**Desde la terminal.** Es equivalente y conviene conocerlo:

```bash
python -m venv .venv
source .venv/bin/activate          # macOS y Linux
.venv\Scripts\activate             # Windows (PowerShell o cmd)
pip install pandas matplotlib ipykernel
pip freeze > requirements.txt
```

Una vez seleccionado el entorno, cada terminal nueva que abra en VS Code lo activa sola.

:::{tip} No versione el entorno
Agregue `.venv/` a `.gitignore`. Lo que se comparte es `requirements.txt` (o `environment.yml` en Conda), con el que cualquiera recrea el entorno.
:::

## Ejecutar scripts

Con un archivo `.py` abierto:

- El botón ▷ (*Run Python File*) de la esquina superior derecha ejecuta el archivo completo en la terminal.
- `Shift+Enter` envía la línea o la selección actual a una consola de Python en la terminal, útil para probar fragmentos.
- `Ctrl+F5` ejecuta sin depurar y `F5` ejecuta con el depurador.

## Notebooks de Jupyter

VS Code abre los archivos `.ipynb` en un editor de notebooks propio, sin necesidad de instalar JupyterLab. Para crear uno, ejecute **Create: New Jupyter Notebook** o cree un archivo con extensión `.ipynb`.

1. **Elija el kernel** con el botón *Select Kernel* de la esquina superior derecha: puede ser el `.venv` del proyecto o cualquier entorno de Conda. El entorno necesita el paquete `ipykernel`; si falta, VS Code ofrece instalarlo.
2. **Ejecute celdas** con `Shift+Enter` (ejecuta y pasa a la siguiente) o con el botón ▷ de cada celda. *Run All* ejecuta todo el cuaderno.
3. **Modo comando.** Con `Esc` sale de la edición de la celda y puede usar las teclas de Jupyter: `A` y `B` insertan una celda arriba o abajo, `M` la convierte en Markdown, `Y` en código y `D D` la borra.
4. **Variables.** El botón *Variables* de la barra del cuaderno abre un panel con todas las variables del kernel, su tipo y su tamaño.
5. **DataFrames.** Desde el panel de variables, o con el botón que aparece bajo la salida de un *DataFrame*, se abre **Data Wrangler**, que muestra la tabla completa con filtros, ordenamiento y estadísticas por columna. Las operaciones de limpieza que haga con su interfaz generan el código de pandas correspondiente, que puede copiar al cuaderno.

:::{note} Cuadernos y Git
Los `.ipynb` guardan salidas e imágenes dentro del JSON, lo que produce diferencias enormes en Git. VS Code muestra las diferencias de los cuadernos celda por celda, pero si prefiere archivos más limpios, la ventana interactiva de la siguiente sección es una buena alternativa.
:::

## La ventana interactiva: scripts con celdas

Un archivo `.py` normal se puede dividir en celdas con comentarios `# %%`. VS Code muestra sobre cada uno los enlaces **Run Cell** y **Run Below**, y los resultados aparecen en la **ventana interactiva**, a la derecha, con tablas y gráficos como en un notebook.

```python
# %% Cargar datos
import pandas as pd

url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"
pinguinos = pd.read_csv(url)
pinguinos.head()

# %% Resumen por especie
pinguinos.groupby("species")[["bill_length_mm", "body_mass_g"]].mean().round(1)

# %% Gráfico
pinguinos.plot.scatter(x="flipper_length_mm", y="body_mass_g", alpha=0.6)
```

Así obtiene lo mejor de los dos mundos: la exploración paso a paso de un notebook y un archivo de texto plano que Git compara línea a línea y que se ejecuta como script con `python archivo.py`. El comando **Jupyter: Export Current Python File as Jupyter Notebook** lo convierte en `.ipynb` cuando lo necesite, y **Jupyter: Export to Python Script**, desde un notebook, hace lo contrario.

## Calidad del código

- **Linter y formateador.** Con la extensión **Ruff** y la configuración `"editor.formatOnSave": true` de la [página 3](03-extensiones-configuracion.md), el código se formatea al guardar y los problemas (importaciones sin usar, variables no definidas) se subrayan mientras escribe.
- **Revisión de tipos.** Pylance puede advertir errores de tipo. La opción `python.analysis.typeCheckingMode` acepta `"off"`, `"basic"`, `"standard"` y `"strict"`; `"basic"` es un buen comienzo.
- **Pruebas.** La vista **Testing** (ícono de matraz) descubre y ejecuta pruebas de `pytest` o `unittest`, y marca en el margen del código cuáles pasan y cuáles fallan. Se configura con el comando **Python: Configure Tests**.

## ¿Y R?

Con la extensión **R** (`REditorSupport.r`) y el paquete `languageserver` instalado en R (`install.packages("languageserver")`), VS Code ofrece autocompletado, ejecución de líneas con `Ctrl+Enter` en una consola de R y visor de gráficos. Para documentos con código de R y Python, la extensión **Quarto** permite editar y previsualizar archivos `.qmd`. Si trabaja sobre todo con R, Positron, el editor de Posit basado en el mismo núcleo que VS Code, ofrece una experiencia más cercana a RStudio.

## Práctica

1. Cree un entorno `.venv` en `practica-vscode` con pandas, matplotlib e ipykernel y selecciónelo como intérprete.
2. Copie el script de pingüinos en `explorar.py` y ejecútelo celda por celda en la ventana interactiva.
3. Expórtelo como notebook, abra el *DataFrame* `pinguinos` en Data Wrangler y filtre una especie.
4. Guarde `pip freeze > requirements.txt` y agregue `.venv/` a un archivo `.gitignore`.
