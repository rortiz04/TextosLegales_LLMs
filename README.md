# Proyecto: Extracción de Metadatos y Generación de Síntesis

Este repositorio contiene el código y las instrucciones necesarias para realizar tareas de **extracción de metadatos** y **generación de síntesis** a partir de textos legales utilizando el modelo **Llama-3.2-11B-Vision-Instruct**.

## Descripción del Proyecto

El objetivo de este proyecto es automatizar dos tareas clave en el tratamiento de textos jurídicos:

1. **Extracción de Metadatos**: Identificar y extraer información relevante como la sede, el juez, la fecha y la resolución de los textos legales.
2. **Generación de Síntesis**: Crear resúmenes concisos y coherentes de textos legales.

Estas tareas son parte de un enfoque de procesamiento de lenguaje natural aplicado al ámbito jurídico, con el objetivo de optimizar procesos manuales y reducir la carga de trabajo.

## Tecnologías Utilizadas

- **[Transformers](https://huggingface.co/docs/transformers/)**: Biblioteca para trabajar con modelos de lenguaje preentrenados.
- **Python**: Lenguaje de programación principal.
- **CUDA**: Para la aceleración en GPU.
- **Torch**: Framework para machine learning.
- **Modelo Llama-3.2-11B-Vision-Instruct**: Modelo preentrenado especializado.

## Requisitos

Antes de comenzar, asegúrate de tener instaladas las siguientes herramientas:

- Python 3.8 o superior
- CUDA 11.7 o superior (para la aceleración en GPU)
- Bibliotecas requeridas:
  ```bash
  pip install transformers torch tqdm

## Configuración y Ejecución

# 1. Clonar el repositorio
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio

# 2. Configurar el modelo
# El código utiliza el modelo preentrenado meta-llama/Llama-3.2-11B-Vision-Instruct.
# Asegúrate de tener acceso al modelo desde Hugging Face:
# https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct

# 3. Preparar los datos
# Asegúrate de que los textos legales estén en formato .txt y colócalos en la carpeta data/input.

# 4. Ejecutar el script principal
python main.py

# 5. Personalizar configuraciones (opcional)
# Los parámetros configurables incluyen:
# - max_new_tokens: Número máximo de tokens generados.
# - temperature: Controla la diversidad de la generación.
# - min_new_tokens: Número mínimo de tokens generados.

## Estructura del Proyecto

├── data/
│   ├── input/           # Textos legales en formato .txt
│   └── output/          # Resultados generados (JSONL)
├── main.py              # Código principal
├── README.md            # Documentación
└── requirements.txt     # Lista de dependencias

## Resultados
## Los resultados se guardan en formato JSONL y contienen:

##Metadatos extraídos.
##Síntesis generada.
##Tiempo de procesamiento por tarea.
##Ejemplo de salida:

{
  "decoded_metadata": "Sede: Córdoba, Dependencia: Civil...",
  "decoded_sintesis": "En este fallo se analizan...",
  "total_time": 12.34
}