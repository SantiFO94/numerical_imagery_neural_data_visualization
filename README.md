## Plantilla de README

### 1) Objetivo
- Analizar y procesar un dataset de señales neuronales (EEG) para identificar patrones de activación cerebral. El objetivo es automatizar la limpieza de datos, extraer características relevantes en el dominio del tiempo y la frecuencia, y generar visualizaciones que permitan comparar el comportamiento entre diferentes dispositivos y estímulos.

### 2) Dataset
- Fuente: Archivos de texto (.txt) generados por dispositivos Emotiv EPOC e Insight pertenecientes al dataset 1.2M Brain Signal Data.
- Nº filas/columnas: Variable (depende del archivo cargado). Se limita en código a 5000 registros para facilitar las pruebas.
- Variables clave: Columnas de datos numéricos y categóricos para análisis
    -id, event, device, channel, code, size  

### 3) Preguntas
- ¿Qué características nuevas se pueden derivar de la limpieza de datos?
- ¿Existe activación bilateral o es unilateral?
- ¿Qué lobulo cortical presenta la mayor activación?
- ¿Existen diferencias de activación entre distintos estimulos?
- ¿Existen diferencias significativas en la señal neuronal entre los dispositivos Emotiv EPOC e Insight?
- ¿Qué bandas de frecuencia (Delta, Theta, Alpha, Beta, Gamma) presentan mayor potencia bajo estímulos específicos?


### 4) Data issues & fixes
- Tipos de datos: Conversión de columnas de metadatos representados por números a valores numéricos.
- Formato de señal: La señal venía como una cadena de texto representando una lista; se implementó parse_strings_list para convertirla a listas de numeros decimales.
- Tratamiento de registros sin datos: Eliminación de registros sin señal registrada.

### 5) Pipeline
- raw .txt → io.txt_transform_csv → cleaning.clean → features.build_features → io.save_csv_file → viz.plot

### 6) Hallazgos
- **Actividad cortical:** Se observa actividad bilateral para los estimulos analizados, presentándose una ligera activación mayor del hemisferio derecho, normalmente más especializado en las tareas de cálculo de magnitudes y con un fuerte componente en la atención espacial, encajando con la tarea realizada de visualización numérica. Además se ha visto una mayor actividad frontotemporal, también asociada a la realización de tareas, mantenimiento de la atención y toma de decisiones. *Es necesario apuntar que no se pueden descartar con este estudio preliminar posibles artefactos o problemas técnicos debidos a los electrodos usados. Sería necesario realziar un estudio más profundo del comportamiento de cada electrodo individual para detectar posibles fallos de contacto o señales aberrantes*
- **Dispositivo EPOC vs Insight:** Gracias al analisis de potencia absoluta por estimulo se pudo detectar una mayor oscilación de señal en el dispositivo Insight, sugiriendo una mayor fiabilidad en la detección de señales EEG del dispositivo Epoc, aunque también podría deberse al mayor número de electrodos utilizados en este último.
- **Bandas de frecuencia:** Se observa que las frecuencias más representadas en el analisis de potencia relativa corresponden a las bandas Delta (0.5, 4) y Beta (13, 30), aunque las bandas más interesantes en el analisis de tareas cognitivas como las de este estudio corresponden a la Theta (4, 8) y Alpha (8, 12), asociadas a tareas cognitivas. En estas últimas observamos una buena consistencia en la potencia relativa presentada por cada estímulo y cada dispositivo. Sería interesante analizar estas bandas en más detalle para intentar descubrir patrones que permitan diferenciar con más precisión entre los diferentes estímulos.

### 7) Estructura del proyecto
- data/: Contiene los archivos raw/ (.txt) y processed/ (.csv).
- notebooks/: Contiene eda.ipynb para la exploración de datos.
- src/: Funciones reutilizables:
    - io.py: Transformación, carga y guardado.
    - cleaning.py: Limpieza y validación.
    - features.py: Extracción de características temporales y de frecuencia.
    - viz.py: Visualizaciones de datos.
- main.py: Punto de entrada del pipeline completo.
```
project/
├── main.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   └── eda.ipynb
├── src/
│   ├── __init__.py
│   ├── io.py
│   ├── cleaning.py
│   ├── config.py
│   ├── features.py
│   ├── viz.py
│   └── utils.py
├── README.md
├── .gitignore
└── requirements.txt
```
### 8) Cómo ejecutar
- Descargar los datasets 1.2M Brain Signal Data: https://www.kaggle.com/datasets/vijayveersingh/1-2m-brain-signal-data/data
- Copiarlos a la carpeta data/raw
- `pip install -r requirements.txt`
- Ejecutar pipeline: `python main.py`
- (Opcional) Abrir y ejecutar: `notebooks/eda.ipynb`



