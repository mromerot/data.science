---
title: Datasets, Spaces y el curso oficial
short_title: 3. Datasets, Spaces y el curso
subtitle: Cargar y procesar datos, evaluar un modelo, publicar una demo y seguir aprendiendo
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Cargar datasets del Hub y archivos propios con la librería `datasets`, filtrarlos y transformarlos, evaluar un modelo con datos etiquetados, descargar archivos del Hub desde Python y publicar una demo en un Space con Gradio.
:::

## La librería `datasets`

`datasets` descarga y procesa conjuntos de datos de forma eficiente: guarda los datos en formato Apache Arrow en disco, de modo que puede trabajar con tablas más grandes que la memoria, y lleva una caché para no repetir descargas ni cálculos.

```bash
pip install datasets
```

### Cargar un dataset del Hub

[SIB-200](https://huggingface.co/datasets/Davlan/sib200) es un dataset de clasificación de temas en más de 200 idiomas, construido sobre frases del corpus Flores-200 (licencia CC BY-SA 4.0). Cada idioma es una configuración; el español es `spa_Latn`:

```python
from datasets import load_dataset

sib = load_dataset("Davlan/sib200", "spa_Latn")
sib
```

```text
DatasetDict({
    train: Dataset({
        features: ['index_id', 'category', 'text'],
        num_rows: 701
    })
    validation: Dataset({
        features: ['index_id', 'category', 'text'],
        num_rows: 99
    })
    test: Dataset({
        features: ['index_id', 'category', 'text'],
        num_rows: 204
    })
})
```

Un `DatasetDict` reúne las particiones (*splits*) de entrenamiento, validación y prueba. Cada fila es un diccionario:

```python
sib["train"][0]
```

```text
{'index_id': 431, 'category': 'geography', 'text': 'Tres de los lados de Turquía están rodados por mares: el oeste, por el Mar Egeo; el norte, por el Mar Negro y el sur, por el Mediterráneo.'}
```

### Cargar sus propios archivos

La misma función lee CSV, JSON, Parquet o texto, locales o desde una URL. Este es el censo de arbolado urbano de Los Rosales (Bogotá) que se usa en el [ejemplo de la página 4](04-ejemplo-arboles.md), con datos abiertos del Jardín Botánico de Bogotá (CC BY 4.0):

```python
url = "https://raw.githubusercontent.com/mromerot/web/main/datascience/_colab/censo_arbolado_rosales.csv"
censo = load_dataset("csv", data_files=url)["train"]
censo
```

```text
Dataset({
    features: ['lon', 'lat', 'especie', 'altura_m', 'anio_censo'],
    num_rows: 3288
})
```

### Filtrar, transformar y pasar a pandas

`filter` conserva las filas que cumplen una condición y `map` agrega o modifica columnas. Ambas guardan el resultado en la caché:

```python
altos = censo.filter(lambda fila: fila["altura_m"] is not None and fila["altura_m"] >= 15)
print(altos.num_rows)

censo = censo.map(lambda fila: {"reciente": fila["anio_censo"] >= 2020})
df = censo.to_pandas()
print(df["especie"].value_counts().head(5))
print(round(df["reciente"].mean(), 3))
```

```text
143
especie
Sauco                              459
Jazmin del cabo, laurel huesito    320
Eucalipto plateado                 228
Acacia japonesa                    199
Guayacan de Manizales              151
Name: count, dtype: int64
0.345
```

Hay 143 árboles de 15 m o más, el saúco es la especie más registrada y solo el 34,5 % de los registros es de 2020 en adelante. Para análisis tabulares como este, pandas basta; la ventaja de `datasets` aparece con colecciones grandes de textos o imágenes que se pasan a un modelo.

:::{note} Columnas perezosas
En las versiones recientes de `datasets`, `sib["test"]["text"]` no devuelve una lista sino un objeto `Column` que lee los datos a medida que se necesitan. Si una función espera una lista, por ejemplo un pipeline, conviértala con `list(...)`.
:::

## Evaluar un modelo con datos etiquetados

En la [página 2](02-transformers.md) el clasificador *zero-shot* acertó con un texto sobre deslizamientos. ¿Qué tan bien funciona en general? SIB-200 trae la respuesta correcta de cada frase, así que podemos medirlo con una muestra de la partición de prueba:

```python
from transformers import pipeline

zero_shot = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
etiquetas = {
    "science/technology": "ciencia y tecnología", "travel": "viajes", "politics": "política",
    "sports": "deportes", "health": "salud", "entertainment": "entretenimiento", "geography": "geografía",
}

muestra = sib["test"].shuffle(seed=42).select(range(60))
resultados = zero_shot(list(muestra["text"]), candidate_labels=list(etiquetas.values()), batch_size=8)

prediccion = [r["labels"][0] for r in resultados]
real = [etiquetas[c] for c in muestra["category"]]
exactitud = sum(p == r for p, r in zip(prediccion, real)) / len(real)
print(f"Exactitud: {exactitud:.1%}")
```

```text
Exactitud: 51.7%
```

Acertó 31 de 60 frases. Con siete categorías, elegir al azar acertaría alrededor del 14 %, así que el modelo sí entiende algo de los temas, pero una de cada dos frases queda mal clasificada: no serviría para clasificar documentos sin revisión humana. Las opciones para mejorar son probar otras formulaciones de las etiquetas, usar un modelo más grande o, con los 701 ejemplos de entrenamiento, ajustar un clasificador propio (*fine-tuning*), que es el tema de los capítulos avanzados del curso.

:::{tip} Tiempo de ejecución
Cada frase se compara con las siete etiquetas, así que son 420 pasadas por el modelo. En CPU tarda varios minutos; con la GPU de Colab, mucho menos.
:::

`shuffle(seed=42)` hace la muestra reproducible: con la misma semilla, cualquiera obtiene las mismas 60 frases y puede verificar el resultado.

## Descargar archivos del Hub: `huggingface_hub`

La librería `huggingface_hub`, que `transformers` y `datasets` usan por debajo, permite descargar archivos sueltos y consultar el Hub desde Python:

```python
import json
from huggingface_hub import hf_hub_download

ruta = hf_hub_download(repo_id="pysentimiento/robertuito-sentiment-analysis", filename="config.json")
json.load(open(ruta))["id2label"]
```

```text
{'0': 'NEG', '1': 'NEU', '2': 'POS'}
```

`hf_hub_download` devuelve la ruta del archivo en la caché local. Desde la terminal, el equivalente es `hf download pysentimiento/robertuito-sentiment-analysis config.json`.

También puede buscar modelos con código, por ejemplo los clasificadores de texto en español más descargados:

```python
from huggingface_hub import HfApi

for modelo in HfApi().list_models(pipeline_tag="text-classification", filter="es", sort="downloads", limit=5):
    print(modelo.id, modelo.downloads)
```

El resultado cambia con el tiempo, a medida que la comunidad publica y usa modelos.

### Publicar sus datos

Con un token de escritura (ver [página 1](01-hugging-face.md)), un dataset procesado se sube al Hub con una línea, y queda con su visor de datos, su ficha y su historial de versiones:

```python
censo.push_to_hub("su-usuario/censo-arbolado-rosales", private=True)
```

Antes de publicar, verifique que la licencia de los datos originales lo permite y escriba una ficha (*dataset card*) que diga de dónde vienen, cómo se procesaron y qué limitaciones tienen.

## Spaces: publicar una demo con Gradio

Un **Space** es una aplicación web alojada en el Hub. Con [Gradio](https://www.gradio.app/), una interfaz para un modelo cabe en un archivo `app.py`:

```python
import gradio as gr
from transformers import pipeline

clasificador = pipeline("text-classification", model="pysentimiento/robertuito-sentiment-analysis")


def analizar(texto):
    return {r["label"]: r["score"] for r in clasificador(texto, top_k=None)}


gr.Interface(
    fn=analizar,
    inputs=gr.Textbox(label="Texto en español"),
    outputs=gr.Label(label="Sentimiento"),
    title="Sentimiento en español",
).launch()
```

`top_k=None` hace que el pipeline devuelva las tres etiquetas con su probabilidad, que `gr.Label` dibuja como barras. Para «El servicio de buses mejoró mucho este año.», `analizar` devuelve `{'POS': 0.86, 'NEU': 0.125, 'NEG': 0.015}` (redondeado).

Para publicarlo:

1. En <https://huggingface.co/new-space>, elija un nombre, el SDK **Gradio** y el hardware gratuito de CPU.
2. Suba `app.py` y un `requirements.txt` con las dependencias (`transformers` y `torch`), desde la web o con Git, porque cada Space es también un repositorio.
3. El Space se construye solo y en unos minutos queda en `https://huggingface.co/spaces/su-usuario/nombre`, listo para compartir.

Puede probar la interfaz antes en Colab: `pip install gradio`, ejecute el código y la demo aparece dentro del cuaderno.

## El curso oficial de Hugging Face

Hugging Face ofrece cursos gratuitos en línea en <https://huggingface.co/learn>. El más conocido, el **Hugging Face Course** (hoy llamado *LLM Course*), está pensado para aprender el ecosistema de procesamiento de lenguaje y *machine learning* de la plataforma desde cero. Cubre desde los fundamentos de la librería `transformers` y los tokenizers hasta el entrenamiento y ajuste fino de modelos, el uso de `datasets` para manejar grandes volúmenes de datos y la publicación de modelos y demos en el Hub.

El curso combina lecciones escritas con una serie de videos cortos en el canal oficial de YouTube de Hugging Face (los de esta sección provienen de ahí) y tiene traducciones a varios idiomas, entre ellos el español. Hay además cursos de visión por computador, audio, agentes de IA y aprendizaje por refuerzo.

:::{iframe} https://www.youtube.com/embed/00GKzGyWFEs
:width: 100%
Welcome to the Hugging Face course.
:::

## Práctica

1. Cargue SIB-200 en otro idioma que conozca (por ejemplo `por_Latn` o `eng_Latn`) y compare el número de frases por categoría con el español.
2. Repita la evaluación *zero-shot* cambiando las etiquetas por frases más descriptivas («noticia sobre deportes», «texto sobre salud»…). ¿Mejora la exactitud?
3. Con el censo, calcule con `filter` cuántos árboles se registraron antes de 2010 y compárelo con el resultado en pandas.
4. Cree un Space con la demo de sentimiento y compártalo.
