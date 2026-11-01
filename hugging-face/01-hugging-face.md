---
title: Hugging Face y el Hub
short_title: 1. Hugging Face y el Hub
subtitle: Modelos, datasets y aplicaciones de IA abiertos
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Entender qué ofrece Hugging Face, encontrar modelos y datasets en el Hub, leer una ficha de modelo (*model card*) con ojo crítico y configurar una cuenta y un token de acceso de forma segura.
:::

## ¿Qué es Hugging Face?

Hugging Face es una plataforma y comunidad de inteligencia artificial dedicada a la construcción de herramientas de aprendizaje automático de código abierto. A menudo se le describe como el «GitHub del *machine learning*», ya que permite alojar, compartir y descubrir modelos, conjuntos de datos y aplicaciones creadas por miles de investigadores, empresas y desarrolladores en todo el mundo.

Su ecosistema se organiza principalmente en tres pilares: **Models** (modelos preentrenados listos para usar), **Datasets** (conjuntos de datos para entrenar y evaluar modelos) y **Spaces** (aplicaciones y demos interactivas). A esto se suma su famosa librería `transformers`, que estandarizó el acceso a modelos de última generación en procesamiento de lenguaje natural, visión por computador y audio.

:::{iframe} https://www.youtube.com/embed/qP9mbY3wuWk
:width: 100%
What is Hugging Face? - Models, Datasets & Spaces.
:::

## El Hub: modelos, datasets y Spaces

El **Hugging Face Hub** (<https://huggingface.co>) es el repositorio central de la plataforma, con cientos de miles de modelos y decenas de miles de datasets disponibles públicamente. Cada modelo cuenta con una «model card» que documenta su arquitectura, su uso previsto, sus limitaciones y ejemplos de código para implementarlo en pocas líneas.

Los **Spaces** permiten publicar demos interactivas usando frameworks como Gradio o Streamlit, de forma gratuita y sin necesidad de gestionar infraestructura propia, lo que facilita mostrar el funcionamiento de un modelo a cualquier persona directamente desde el navegador.

:::{iframe} https://www.youtube.com/embed/XvSGPZFEjDY
:width: 100%
Navigating the Model Hub (curso de Hugging Face).
:::

### Buscar un modelo

La página <https://huggingface.co/models> tiene filtros en la columna izquierda. Los más útiles son:

| Filtro | Ejemplo | Para qué |
| --- | --- | --- |
| **Tasks** | *Text Classification*, *Image Segmentation*, *Object Detection* | Qué hace el modelo. |
| **Languages** | *Spanish* | Modelos entrenados o ajustados en español. |
| **Libraries** | *Transformers*, *PyTorch*, *GGUF* | Con qué se carga. |
| **Licenses** | *apache-2.0*, *mit*, *cc-by-4.0* | Qué se puede hacer con él. |

Ordene por *Most downloads* o *Trending* para empezar por modelos probados por mucha gente. Cada modelo se identifica como `usuario_u_organización/nombre`, por ejemplo [`pysentimiento/robertuito-sentiment-analysis`](https://huggingface.co/pysentimiento/robertuito-sentiment-analysis), un clasificador de sentimiento para textos en español. Ese identificador es lo que se escribe en el código.

### Qué hay dentro de un repositorio de modelo

Cada modelo es un repositorio Git con historial de versiones. La pestaña **Files and versions** muestra archivos como estos:

| Archivo | Contenido |
| --- | --- |
| `README.md` | La ficha del modelo (*model card*). |
| `config.json` | La arquitectura y sus parámetros, incluidas las etiquetas de salida (por ejemplo `{0: "NEG", 1: "NEU", 2: "POS"}`). |
| `model.safetensors` | Los pesos entrenados. `safetensors` es un formato seguro que, a diferencia de los antiguos `.bin` de PyTorch, no puede ejecutar código al cargarse. |
| `tokenizer.json`, `tokenizer_config.json` | El *tokenizer* que convierte el texto en números (ver [página 2](02-transformers.md)). |

### Leer una ficha de modelo con ojo crítico

Antes de usar un modelo en un trabajo, busque en su ficha:

1. **Uso previsto y limitaciones.** ¿Con qué datos se entrenó? Un clasificador entrenado con tuits puede fallar con documentos oficiales; un detector de árboles entrenado en bosques puede fallar en una ciudad, como se ve en el [ejemplo de esta sección](04-ejemplo-arboles.md).
2. **Evaluación.** ¿Con qué métricas y sobre qué datos se midió? ¿Hay resultados en español?
3. **Sesgos.** Las buenas fichas advierten de sesgos conocidos, por ejemplo de género o de variedad dialectal.
4. **Licencia.** Va en la cabecera de la ficha. Licencias como `apache-2.0` o `mit` permiten casi cualquier uso; otras restringen el uso comercial (`cc-by-nc-4.0`) o imponen condiciones de uso responsable (familia OpenRAIL). Algunos modelos están **restringidos** (*gated*): hay que aceptar sus condiciones con una cuenta antes de descargarlos. Si la ficha no declara licencia, no asuma que el uso es libre.
5. **Cita.** Muchas fichas incluyen la referencia del artículo que deben citar los trabajos que usen el modelo.

## Cuenta y token de acceso

Descargar modelos públicos no requiere cuenta, pero la necesitará para modelos restringidos, para subir sus propios modelos o datasets y para crear Spaces.

1. Cree una cuenta gratuita en <https://huggingface.co/join>.
2. En **Settings → Access Tokens**, cree un token. Elija el tipo **Read** para descargar, **Write** si va a publicar, o **Fine-grained** para limitar el token a repositorios y permisos concretos, la opción más segura.
3. Use el token sin escribirlo en el código:

| Entorno | Cómo |
| --- | --- |
| **Google Colab** | Panel de **Secretos** (ícono de llave en la barra izquierda): cree un secreto llamado `HF_TOKEN` y active el acceso para el cuaderno. Las librerías de Hugging Face lo leen solas. |
| **Su computador** | En la terminal, `hf auth login` y pegue el token cuando lo pida; queda guardado para las siguientes sesiones. En versiones antiguas de la librería el comando es `huggingface-cli login`. |
| **Servidores y GitHub Actions** | Variable de entorno `HF_TOKEN`, guardada como secreto del servicio. |

:::{danger} Nunca publique su token
Un token escrito en un notebook o en un script termina, tarde o temprano, en un repositorio público. Si eso ocurre, revóquelo de inmediato en **Settings → Access Tokens** y cree uno nuevo.
:::

## Dónde quedan los modelos descargados

La primera vez que usa un modelo, las librerías lo descargan a una caché local (`~/.cache/huggingface/hub` en macOS y Linux, `C:\Users\<usuario>\.cache\huggingface\hub` en Windows) y las siguientes veces lo leen de ahí. Los modelos pesan desde decenas de megabytes hasta cientos de gigabytes; para mover la caché a otro disco, defina la variable de entorno `HF_HOME`. El comando `hf cache ls` lista lo descargado y cuánto ocupa.

## Ruta de esta sección

| Página | Qué aprenderá |
| --- | --- |
| [1. Hugging Face y el Hub](01-hugging-face.md) | El Hub, las fichas de modelo, licencias, cuenta y token. |
| [2. Transformers y tokenizers](02-transformers.md) | Usar modelos con `pipeline()` y entender qué pasa por dentro. |
| [3. Datasets, Spaces y el curso](03-datasets-spaces.md) | Cargar y procesar datos con `datasets`, publicar demos con Gradio y seguir aprendiendo. |
| [4. Ejemplo: contar árboles](04-ejemplo-arboles.md) | Un caso completo en Google Colab con modelos de visión sobre imágenes aéreas de Bogotá. |

## Práctica

1. En <https://huggingface.co/models>, filtre por *Text Classification* y *Spanish* y ordene por descargas. Anote los tres primeros modelos y su licencia.
2. Abra la ficha de [`MoritzLaurer/mDeBERTa-v3-base-mnli-xnli`](https://huggingface.co/MoritzLaurer/mDeBERTa-v3-base-mnli-xnli). ¿Con qué datos se entrenó? ¿En qué idiomas se evaluó?
3. Cree una cuenta y un token de tipo *Read*, y guárdelo como secreto `HF_TOKEN` en Google Colab.
