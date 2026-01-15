---
title: Configurar Myst
date: 2025-01-11
authors:
  - name: Mauricio Romero T.
    github: mauriciort
exports:
  - format: pdf
---

Existe una sólida documentación de la instalación y funcionamiento de Myst en su sitio oficial (<https://mystmd.org/>). Para nosotros hispanohablantes facilita emplear la opción de traducción del navegador.

## Instalación de Myst
-   Revise el tutorial por extenso aquí: [*Link*](https://mystmd.org/guide/quickstart)
-   Instale Python, MyST Markdown CLI, y VS-Code
-   Revise en consola si Myst se instaló correctamente: myst -v
-   Descargue el contenido de ejemplo y navegue hasta la carpeta
    -   `git clone https://github.com/jupyter-book/`
    -   `mystmd-quickstart.git` -`cd mystmd-quickstart`
-   aparecera este mensaje ” 💾 Writing new project and site config file: myst.yml — ? Would you like to run myst start now? (Y/n)”
-   Luego podrá abrir el nuevo proyecto en su navegador con `start myst`.

## Configuración de Myst
Myst se configura principalmente a través de un archivo llamado `myst.yml` ubicado en la raíz del proyecto. Este archivo define la estructura del contenido, las opciones de compilación y otros parámetros importantes para el funcionamiento de Myst.

## Estructura del archivo myst.yml
El archivo `myst.yml` se organiza en varias secciones clave que permiten personalizar el comportamiento de Myst. A continuación, se describen las secciones más importantes:

### **TOC (Table of Contents)**
Define la estructura del contenido del proyecto, especificando los archivos y su orden de aparición. `yaml     toc:       - file: introduccion.md       - file: capitulo1.md       - file: capitulo2.md` \### **Build Options** Configure las opciones de compilación, como el formato de salida (PDF, HTML, etc.) y las opciones específicas para cada formato. `yaml     build:       pdf:         latex_engine: xelatex       html:         theme: myst-theme` \### **Extensions** Habilita o deshabilita extensiones específicas de Myst para agregar funcionalidades adicionales. `yaml     extensions:       - myst_math       - myst_tables` \### **Metadata** Define metadatos globales para el proyecto, como el título, autor y fecha. \`\`\`yaml metadata: title: "Mi Proyecto Myst"

### Visualización de Myst en navegador
-   Abra el proyecto en su navegador con `start myst`.
-   Redenrice el proyecto con `build myst`.

### Publicar proyecto en GitHub Pages
-   Siga el tutorial oficial aquí: link
-   Configure GitHub Actions para despliegue automático.

### Instale jupyterlab-myst?
jupyterlab-myst es una extensión para JupyterLab que te permite renderizar y trabajar con MyST Markdown directamente dentro del entorno de JupyterLab, similar a como funciona en tu sitio web MyST pero mientras editas los notebooks. Permite:
* Renderizar MyST Markdown directamente en JupyterLab
* Usar expresiones {eval} para evaluar código inline
* Integrar widgets interactivos (ipywidgets)
* Editar listas de tareas en markdown
* Visualizar referencias cruzadas, figuras numeradas, etc.

![Demo de jupyterlab-myst](https://github.com/jupyter-book/jupyterlab-myst/blob/main/images/walkthrough.gif)
