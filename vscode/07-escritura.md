---
title: Escritura y documentación con VS Code
short_title: 7. Escritura y documentación
subtitle: "VS Code para no desarrolladores: Markdown, MyST y Quarto"
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Usar VS Code como editor de textos técnicos: escribir y previsualizar Markdown, revisar la ortografía en español, trabajar con MyST y Quarto y llevar el historial de los documentos con Git.
:::

## VS Code para no desarrolladores

Aunque nació como un editor para programar, VS Code se ha convertido en una herramienta de propósito general útil incluso para quienes nunca han escrito una línea de código. Sirve para redactar documentos en Markdown, organizar notas, llevar control de versiones de escritos con Git, gestionar archivos de proyectos, e incluso trabajar con asistentes de IA integrados para tareas creativas o de escritura.

Gracias a su extensísimo marketplace de extensiones, cualquier persona puede personalizar VS Code para tareas muy específicas: temas visuales, resaltado para formatos como YAML o CSV, correctores ortográficos, integración con Google Drive, y mucho más, todo sin necesidad de conocimientos de programación.

:::{iframe} https://www.youtube.com/embed/uQV8uEzgxHo
:width: 100%
VS Code For Non-Developers.
:::

## Markdown con vista previa

VS Code trae soporte completo para Markdown, sin extensiones:

| Acción | Windows / Linux | macOS |
| --- | --- | --- |
| Vista previa en una pestaña | `Ctrl+Shift+V` | `Cmd+Shift+V` |
| Vista previa al lado, sincronizada | `Ctrl+K V` | `Cmd+K V` |
| Esquema del documento | Vista *Outline* del Explorador | igual |
| Ir a un encabezado | `Ctrl+Shift+O` | `Cmd+Shift+O` |

Otras funciones útiles para escribir:

- **Pegar imágenes.** Si copia una captura de pantalla y la pega con `Ctrl+V` en un archivo Markdown, VS Code guarda la imagen en el proyecto y escribe el enlace `![](...)`.
- **Enlaces entre archivos.** Al escribir `[texto](` aparecen sugerencias de los archivos del proyecto, y al escribir `#` dentro del enlace, de los encabezados del archivo. Si cambia el nombre de un archivo, VS Code puede actualizar los enlaces que lo mencionan.
- **Modo Zen.** `Ctrl+K Z` oculta todo menos el texto; `Esc Esc` sale.
- **Ajuste de línea.** Con `"editor.wordWrap": "on"` para Markdown (ver la [página 3](03-extensiones-configuracion.md)), los párrafos largos se ajustan a la ventana sin introducir saltos de línea.

Dos extensiones complementan el soporte de base: **Markdown All in One** (`yzhang.markdown-all-in-one`), que agrega atajos como `Ctrl+B` para negrita y genera tablas de contenido, y **markdownlint** (`DavidAnson.vscode-markdownlint`), que señala problemas de estilo como encabezados mal anidados.

## Ortografía en español

Instale **Code Spell Checker** y su diccionario en español (`streetsidesoftware.code-spell-checker-spanish`). Luego indique los idiomas en la configuración:

```json
{
  "cSpell.language": "en,es"
}
```

Las palabras desconocidas se subrayan; con `Ctrl+.` sobre ellas puede ver sugerencias o agregarlas al diccionario del usuario o del proyecto (útil para términos técnicos como *geoprocesamiento* o nombres propios).

## MyST: escribir este libro

Este libro está escrito en [MyST Markdown](https://mystmd.org/) y VS Code es un buen entorno para editarlo:

1. Clone el repositorio con **Git: Clone** (`https://github.com/mromerot/data.science`).
2. Instale la extensión **MyST-Markdown** (`ExecutableBookProject.myst-highlight`), que resalta directivas como `:::{note}` y roles como `{doi}`.
3. Instale MyST (requiere Node.js) y arranque el servidor de vista previa en la terminal integrada:

```bash
npm install -g mystmd
myst start
```

4. Abra en el navegador la dirección que indica la terminal (normalmente `http://localhost:3000`). Cada vez que guarda un archivo, la página se actualiza.

La vista previa de Markdown de VS Code no interpreta las directivas de MyST; para ver el resultado real, use `myst start`. En la sección [MyST Markdown](../myst/config-myst.md) de este libro encontrará más detalles.

## Quarto

La extensión **Quarto** (`quarto.quarto`) agrega resaltado, autocompletado de opciones YAML y el comando **Quarto: Preview** (`Ctrl+Shift+K`), que renderiza el documento `.qmd` y lo muestra en un panel al lado del editor. También ejecuta celdas de código de Python o R dentro del `.qmd`, como un notebook, y ofrece un **editor visual** (comando **Quarto: Edit in Visual Mode**) parecido a un procesador de textos.

## Datos y configuraciones

Gran parte del trabajo con datos consiste en revisar archivos de texto estructurado:

- **CSV:** con **Rainbow CSV**, cada columna tiene un color y el comando *Align CSV columns* las alinea para leerlas mejor.
- **JSON:** viene incluido, con formato (`Shift+Alt+F`) y validación de sintaxis.
- **YAML:** la extensión de Red Hat valida archivos como `myst.yml` o los flujos de GitHub Actions.

## Control de versiones para textos

Git no es solo para código. Con un repositorio por documento o proyecto, cada versión de un informe, un artículo o una tesis queda guardada con una descripción, se pueden comparar dos versiones palabra por palabra y nunca más hará falta guardar `informe_final_v3_ahora_si.docx`. Todo lo necesario está en la [página 6](06-git.md).

:::{tip} Comparar dos archivos cualesquiera
Seleccione dos archivos en el Explorador con `Ctrl+clic`, haga clic derecho y elija **Compare Selected**. Desde la terminal: `code --diff version1.md version2.md`.
:::

## Práctica

1. Cree un archivo `informe.md` con títulos, una lista, una tabla y una imagen pegada desde el portapapeles. Ábralo con la vista previa al lado.
2. Configure el corrector ortográfico en español y corrija los errores que señale.
3. Clone este libro, ejecute `myst start` y cambie una frase de una página para ver la actualización en vivo.
