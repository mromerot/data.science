---
title: La librería Transformers y los tokenizers
short_title: 2. Transformers y tokenizers
subtitle: Usar modelos preentrenados con pocas líneas y entender qué pasa por dentro
authors:
  - name: Mauricio Romero T.
---

:::{important} Objetivos
Usar `pipeline()` para clasificar textos en español, conocer las tareas disponibles, entender cómo un *tokenizer* convierte texto en números y reproducir paso a paso lo que hace un pipeline: tokenizar, pasar por el modelo y convertir la salida en probabilidades.
:::

## La librería Transformers y el pipeline

La librería `transformers` de Hugging Face ofrece una interfaz unificada para descargar y usar miles de modelos preentrenados con muy poco código. Su componente más sencillo es la función `pipeline()`, que encapsula todo el flujo de trabajo (preprocesamiento del texto, inferencia del modelo y posprocesamiento de resultados) en una sola llamada, permitiendo tareas como clasificación de texto, generación de texto o reconocimiento de entidades en pocas líneas de código.

Por debajo de esta simplicidad, la librería se apoya en PyTorch, el framework de *deep learning* más usado en investigación, lo que da flexibilidad tanto a quienes solo quieren usar un modelo como a quienes desean entrenarlo o ajustarlo (*fine-tuning*).

:::{iframe} https://www.youtube.com/embed/1pedAIvTWXk
:width: 100%
What happens inside the pipeline function? (PyTorch), curso de Hugging Face.
:::

## Preparación

En Google Colab, `transformers` y `torch` ya vienen instalados. En su computador, dentro de un entorno virtual (ver [VS Code: Python y Jupyter](../vscode/04-python-jupyter.md)):

```bash
pip install transformers torch
```

Los ejemplos de esta página se ejecutaron con `transformers` 5.22 y `torch` 2.15 en CPU. Los modelos se descargan la primera vez y quedan en la caché.

## Primer pipeline: sentimiento en español

```python
from transformers import pipeline

clasificador = pipeline("text-classification", model="pysentimiento/robertuito-sentiment-analysis")
clasificador([
    "El nuevo parque quedó hermoso y lleno de árboles.",
    "Otra vez se inundó la calle y nadie responde.",
    "La reunión de la junta es el martes a las 6 p. m.",
])
```

```text
[{'label': 'POS', 'score': 0.9737576842308044},
 {'label': 'NEG', 'score': 0.9509337544441223},
 {'label': 'NEU', 'score': 0.8930394649505615}]
```

El modelo es [RoBERTuito](https://huggingface.co/pysentimiento/robertuito-sentiment-analysis), entrenado con tuits en español del proyecto *pysentimiento*. Para cada texto devuelve la etiqueta más probable (positivo, negativo o neutro) y su puntuación entre 0 y 1. Siempre conviene escribir el nombre del modelo: si se omite, la librería elige uno por defecto, casi siempre en inglés.

## Clasificar sin entrenar: *zero-shot*

¿Y si las categorías que necesita no existen en ningún modelo? La clasificación *zero-shot* usa un modelo de inferencia de lenguaje natural para decidir cuál de las etiquetas que usted propone describe mejor el texto, sin entrenamiento adicional:

```python
zero_shot = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
resultado = zero_shot(
    "Las lluvias de la última semana provocaron deslizamientos en tres veredas del municipio.",
    candidate_labels=["inundación", "deslizamiento", "sismo", "incendio forestal"],
)
list(zip(resultado["labels"], [round(s, 3) for s in resultado["scores"]]))
```

```text
[('deslizamiento', 0.696), ('inundación', 0.301), ('sismo', 0.002), ('incendio forestal', 0.001)]
```

El modelo, multilingüe y con licencia MIT, reparte la probabilidad entre las etiquetas: reconoce el deslizamiento y deja algo para inundación, que también se relaciona con lluvias. Es una herramienta rápida para clasificar reportes, noticias o respuestas abiertas de encuestas, pero hay que medir su desempeño con datos propios antes de confiar en ella; en la [página 3](03-datasets-spaces.md) lo evaluamos con un dataset etiquetado.

## Tareas disponibles

El primer argumento de `pipeline()` es la tarea. Algunas de las más útiles:

| Tarea | Entrada → salida | Ejemplo de uso |
| --- | --- | --- |
| `text-classification` | Texto → etiqueta | Sentimiento, temas, detección de lenguaje ofensivo. |
| `zero-shot-classification` | Texto + etiquetas propias → etiqueta | Clasificar sin datos de entrenamiento. |
| `token-classification` | Texto → entidades | Encontrar nombres de lugares, personas u organizaciones (NER). |
| `fill-mask` | Texto con `[MASK]` → palabras probables | Explorar qué aprendió un modelo de lenguaje. |
| `feature-extraction` | Texto → vector numérico | Búsqueda semántica y agrupamiento de documentos. |
| `text-generation` | Texto o conversación → texto | Resumir, traducir, responder preguntas con un modelo conversacional. |
| `image-classification` | Imagen → etiqueta | Clasificar fotografías o teselas. |
| `object-detection` | Imagen → cajas con etiqueta | Contar objetos en una imagen. |
| `image-segmentation` | Imagen → máscara por píxel | Separar cobertura arbórea, agua o construcciones. |
| `automatic-speech-recognition` | Audio → texto | Transcribir entrevistas. |

Para encontrar modelos de una tarea, use el filtro *Tasks* del Hub (ver [página 1](01-hugging-face.md)).

:::{warning} Cambios en la versión 5 de `transformers`
La versión 5 eliminó los pipelines `translation`, `summarization` y `question-answering`. Esas tareas se hacen ahora con `text-generation` y un modelo conversacional. Si un tutorial antiguo usa `pipeline("translation", ...)` y falla con `KeyError`, esta es la causa. La forma actual:

```python
generador = pipeline("text-generation", model="Qwen/Qwen2.5-0.5B-Instruct")
mensajes = [{"role": "user",
             "content": "Traduce al inglés: El arbolado urbano reduce la temperatura de las calles."}]
salida = generador(mensajes, max_new_tokens=40, do_sample=False)
print(salida[0]["generated_text"][-1]["content"])
```

```text
The urban forest reduces the temperature of streets.
```

Con un modelo tan pequeño (0,5 mil millones de parámetros, Apache 2.0) la traducción es aceptable pero no perfecta: *urban trees* sería más exacto que *urban forest*. Los modelos más grandes traducen mejor, a cambio de más memoria y tiempo.
:::

## Tokenizers

Antes de que un modelo de lenguaje pueda procesar texto, este debe convertirse en números mediante un **tokenizer**. Hugging Face ofrece la librería `tokenizers`, escrita en Rust para lograr un rendimiento muy alto, que se encarga de dividir el texto en tokens (palabras, subpalabras o caracteres), asignarles identificadores numéricos y aplicar el relleno (*padding*) y truncamiento necesarios para que los modelos puedan procesarlos en lotes.

Cada modelo preentrenado en el Hub incluye su propio tokenizer asociado, garantizando que el texto se procese exactamente igual que durante el entrenamiento original del modelo, lo cual es clave para obtener buenos resultados.

:::{iframe} https://www.youtube.com/embed/3umI3tm27Vw
:width: 100%
Fast tokenizer superpowers, curso de Hugging Face.
:::

Veámoslo con el tokenizer de [BETO](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased), un modelo BERT entrenado en español por la Universidad de Chile:

```python
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("dccuchile/bert-base-spanish-wwm-cased")
frase = "La deforestación amenaza los humedales del Magdalena."
tokenizer.tokenize(frase)
```

```text
['La', 'def', '##orestación', 'amenaza', 'los', 'hume', '##dales', 'del', 'Magdalena', '.']
```

Las palabras frecuentes son un solo token; las menos comunes se parten en **subpalabras**, y `##` indica que el fragmento continúa la palabra anterior. Así el vocabulario se mantiene en unas decenas de miles de piezas y aun así el modelo puede representar cualquier palabra.

Cada token tiene un número, que es lo que recibe el modelo:

```python
codificado = tokenizer(frase)
print(codificado["input_ids"])
print(tokenizer.decode(codificado["input_ids"]))
```

```text
[4, 1198, 1951, 25582, 6560, 1065, 12867, 26098, 1072, 23156, 1009, 5]
[CLS] La deforestación amenaza los humedales del Magdalena. [SEP]
```

El tokenizer agregó dos tokens especiales que BERT espera: `[CLS]` al inicio (id 4) y `[SEP]` al final (id 5).

### Lotes, relleno y máscara de atención

Los modelos procesan varios textos a la vez como una matriz, y todas las filas deben tener la misma longitud. El tokenizer **rellena** las frases cortas y crea una **máscara de atención** que indica qué posiciones son texto real (1) y cuáles relleno (0):

```python
lote = tokenizer(["Hola.", "Una frase un poco más larga."], padding=True, return_tensors="pt")
print(lote["input_ids"])
print(lote["attention_mask"])
```

```text
tensor([[   4, 1894, 1009,    5,    1,    1,    1,    1,    1],
        [   4, 1965, 9712, 1049, 1958, 1216, 6072, 1009,    5]])
tensor([[1, 1, 1, 1, 0, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1, 1]])
```

El 1 que rellena la primera fila es el token `[PAD]`. Con `truncation=True`, los textos más largos que el máximo del modelo (512 tokens en BERT) se recortan en lugar de producir un error.

## Qué hace el pipeline por dentro

El pipeline de sentimiento del inicio equivale a estos tres pasos:

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

nombre = "pysentimiento/robertuito-sentiment-analysis"
tokenizer = AutoTokenizer.from_pretrained(nombre)
modelo = AutoModelForSequenceClassification.from_pretrained(nombre)

# 1. Preprocesar: texto -> tensores
entradas = tokenizer(["Otra vez se inundó la calle y nadie responde."], return_tensors="pt")

# 2. Inferencia: tensores -> puntuaciones sin normalizar (logits)
with torch.no_grad():
    logits = modelo(**entradas).logits
print(logits)

# 3. Posprocesar: logits -> probabilidades -> etiquetas
probabilidades = torch.softmax(logits, dim=-1)[0]
{modelo.config.id2label[i]: round(float(p), 3) for i, p in enumerate(probabilidades)}
```

```text
tensor([[ 2.6908, -0.3575, -2.7910]])
{'NEG': 0.951, 'NEU': 0.045, 'POS': 0.004}
```

- Las clases `Auto*` leen el `config.json` del modelo y construyen la arquitectura correcta; no hace falta saber si es BERT, RoBERTa u otra.
- `torch.no_grad()` desactiva el cálculo de gradientes, que solo se necesita para entrenar, y ahorra memoria.
- Los **logits** son puntuaciones sin escala; la función *softmax* los convierte en probabilidades que suman 1. El 0,951 de NEG coincide con el que dio el pipeline.
- `id2label`, guardado en el `config.json`, traduce la posición 0, 1, 2 a NEG, NEU y POS.

Conocer estos pasos es lo que permite ir más allá del pipeline: procesar miles de textos por lotes, extraer los vectores internos del modelo o ajustarlo con datos propios.

## Usar la GPU

Los modelos grandes y las imágenes son mucho más rápidos en GPU. En Colab, active *Entorno de ejecución → Cambiar tipo de entorno → GPU* y pase el dispositivo al pipeline:

```python
clasificador = pipeline("text-classification", model="pysentimiento/robertuito-sentiment-analysis", device="cuda")
```

Para modelos que no caben en una sola GPU, `device_map="auto"` los reparte entre la memoria disponible.

## Práctica

1. Clasifique con el pipeline de sentimiento diez comentarios reales sobre un servicio público de su ciudad. ¿En cuáles se equivoca? ¿Por qué cree que ocurre?
2. Use el pipeline *zero-shot* para clasificar cinco titulares de noticias en las categorías «riesgo de desastres», «salud», «economía» y «deportes».
3. Tokenice con BETO una frase con términos técnicos (por ejemplo *evapotranspiración*, *geomorfología*) y cuente en cuántas subpalabras se divide cada uno.
4. Repita el paso a paso de «Qué hace el pipeline por dentro» con otra frase y compruebe que obtiene la misma probabilidad que con `pipeline()`.
