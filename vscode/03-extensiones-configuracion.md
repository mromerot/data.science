---
title: Extensiones y configuración
short_title: 3. Extensiones y configuración
subtitle: Adaptar VS Code a la ciencia de datos y a cada proyecto
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Instalar y administrar extensiones, escoger un conjunto básico para ciencia de datos, editar la configuración en `settings.json`, separar la configuración personal de la de cada proyecto y usar perfiles.
:::

## El Marketplace de extensiones

VS Code hace poco por sí solo; su fuerza está en las extensiones. La vista **Extensiones** (`Ctrl+Shift+X`, `Cmd+Shift+X` en macOS) busca en el [Visual Studio Marketplace](https://marketplace.visualstudio.com/vscode), instala con un clic y muestra la descripción, el número de instalaciones, la calificación y el editor de cada extensión.

Desde el ícono de engranaje de una extensión instalada puede **desactivarla** solo para el espacio de trabajo actual, útil para no cargar extensiones de R en un proyecto de Python. También se instalan desde la terminal con su identificador:

```bash
code --install-extension ms-python.python
code --list-extensions
```

:::{warning} Las extensiones ejecutan código
Una extensión corre con los mismos permisos que su usuario. Prefiera las de editores verificados (marca azul junto al nombre), con muchas instalaciones y código abierto, y desinstale las que ya no use.
:::

## Extensiones recomendadas para ciencia de datos

| Extensión | Identificador | Para qué |
| --- | --- | --- |
| Python | `ms-python.python` | Intérpretes, entornos y ejecución. Instala también **Pylance** (IntelliSense) y **Python Debugger**. |
| Jupyter | `ms-toolsai.jupyter` | Notebooks `.ipynb` y ventana interactiva. |
| Data Wrangler | `ms-toolsai.datawrangler` | Ver, filtrar y limpiar *DataFrames* de pandas con una interfaz tipo hoja de cálculo que genera el código. |
| Ruff | `charliermarsh.ruff` | Linter y formateador de Python muy rápido. |
| R | `REditorSupport.r` | Edición, ejecución y gráficos de R (requiere el paquete `languageserver` en R). |
| Quarto | `quarto.quarto` | Edición y vista previa de documentos Quarto (`.qmd`). |
| MyST-Markdown | `ExecutableBookProject.myst-highlight` | Resaltado de directivas y roles de MyST, como los de este libro. |
| Rainbow CSV | `mechatroner.rainbow-csv` | Colorea las columnas de archivos CSV y TSV. |
| YAML | `redhat.vscode-yaml` | Validación y autocompletado de YAML, como `myst.yml`. |
| GitLens | `eamodio.gitlens` | Historial y autoría línea a línea en Git. |
| Code Spell Checker | `streetsidesoftware.code-spell-checker` | Corrector ortográfico; con `streetsidesoftware.code-spell-checker-spanish` revisa en español. |

Empiece con pocas: Python, Jupyter y una o dos más según su trabajo. Cada extensión consume memoria y tiempo de arranque.

### Recomendar extensiones a un equipo

Un archivo `.vscode/extensions.json` en el repositorio hace que VS Code sugiera instalar las extensiones del proyecto a quien lo abra:

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-toolsai.jupyter",
    "charliermarsh.ruff",
    "ExecutableBookProject.myst-highlight"
  ]
}
```

## La configuración

*File → Preferences → Settings* (`Ctrl+,`, `Cmd+,` en macOS) abre el editor de configuración, con un buscador y casillas para cada opción. Toda esa configuración se guarda como texto en un archivo `settings.json`, que puede editar directamente con el comando **Preferences: Open User Settings (JSON)**. Editar el JSON es más rápido cuando ya sabe qué quiere y permite copiar la configuración entre computadores.

Un punto de partida razonable para ciencia de datos:

```json
{
  "editor.fontSize": 15,
  "editor.rulers": [88],
  "editor.formatOnSave": true,
  "editor.minimap.enabled": false,
  "files.autoSave": "afterDelay",
  "files.trimTrailingWhitespace": true,
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff"
  },
  "[markdown]": {
    "editor.wordWrap": "on"
  }
}
```

Las claves entre corchetes, como `"[python]"`, aplican la configuración **solo a ese lenguaje**: aquí, Ruff formatea Python al guardar y los archivos Markdown ajustan las líneas largas a la ventana.

### Configuración de usuario y de espacio de trabajo

VS Code combina varios niveles de configuración; el más específico gana:

| Nivel | Dónde se guarda | Úselo para |
| --- | --- | --- |
| Usuario | Carpeta de configuración de su sistema | Preferencias personales: tema, fuente, atajos. Aplica a todo lo que abra. |
| Espacio de trabajo | `.vscode/settings.json` dentro del proyecto | Reglas del proyecto: formateador, intérprete, exclusiones. Se puede versionar con Git para que todo el equipo las comparta. |

En el editor de configuración, las pestañas **User** y **Workspace** indican en qué nivel está escribiendo.

:::{tip} Ocultar ruido en el Explorador
En un proyecto de MyST, la carpeta `_build` crece con cada compilación. Esta configuración de espacio de trabajo la oculta del Explorador y de las búsquedas:

```json
{
  "files.exclude": { "_build": true, "**/.ipynb_checkpoints": true },
  "search.exclude": { "_build": true }
}
```
:::

## Temas, íconos y atajos propios

- **Tema de color:** `Ctrl+K Ctrl+T` (`Cmd+K Cmd+T`) muestra los temas instalados con vista previa inmediata. *Dark Modern* y *Light Modern* vienen por defecto.
- **Íconos de archivo:** comando **Preferences: File Icon Theme**.
- **Atajos:** en el editor de atajos (`Ctrl+K Ctrl+S`) busque un comando, haga doble clic y presione la combinación nueva. VS Code avisa si ya está en uso. Los atajos personalizados quedan en `keybindings.json`.

## Perfiles y sincronización

Un **perfil** (*File → Preferences → Profiles*) es un conjunto con nombre de extensiones, configuración, atajos y tema. Puede tener, por ejemplo, un perfil *Ciencia de datos* con Python y Jupyter, y otro *Escritura* con Markdown, MyST y el corrector ortográfico, y cambiar de uno a otro sin que se mezclen sus extensiones. Cada ventana recuerda el perfil con que se abrió.

**Settings Sync** (el ícono de cuenta, abajo a la izquierda → *Backup and Sync Settings*) guarda la configuración, las extensiones y los perfiles en su cuenta de GitHub o de Microsoft, de modo que un computador nuevo queda igual en minutos.

## Práctica

1. Instale las extensiones Python, Jupyter y Rainbow CSV. Abra un archivo CSV para ver el efecto de la última.
2. Abra su `settings.json` de usuario y agregue `"editor.rulers": [88]` y la configuración `"[markdown]"` del ejemplo.
3. En la carpeta `practica-vscode`, cree `.vscode/settings.json` con `"files.autoSave": "off"`. Compruebe en el editor de configuración que la pestaña **Workspace** muestra ese valor y que prevalece sobre el de usuario.
4. Cree un perfil llamado *Escritura* e instale en él solo el corrector ortográfico.
