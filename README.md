

## Requisitos del Proyecto

Asegúrate de contar con los siguientes requisitos antes de ejecutar el proyecto:

### Herramientas Necesarias
- **Python 3.8 o superior**: Lenguaje de programación principal.
- **CUDA 11.7 o superior**: Para aprovechar la aceleración en GPU (opcional si no se utiliza GPU).

### Dependencias
Instala las siguientes bibliotecas mediante `pip`:
```bash
pip install transformers torch tqdm
```

## Uso

Sigue los pasos a continuación para configurar y ejecutar el proyecto:

### Clonar el Repositorio
Clona este repositorio en tu máquina local y accede al directorio del proyecto:
```bash
git clone https://github.com/tuusuario/tu-repositorio.git
cd tu-repositorio
```

### Configurar el Modelo
El proyecto utiliza el modelo preentrenado **meta-llama/Llama-3.2-11B-Vision-Instruct**. Asegúrate de tener acceso al modelo desde Hugging Face en el siguiente enlace:  
- [Llama-3.2-11B-Vision-Instruct en Hugging Face](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct)

### Preparar los Datos
Coloca los textos legales en formato `.txt` dentro de la carpeta `data/input`. Asegúrate de que estén preprocesados correctamente para su análisis.

### Ejecutar el Script Principal
Para realizar las tareas de extracción de metadatos y generación de síntesis, ejecuta el siguiente comando:
```bash
python main.py
```

### Personalizar configuraciones (opcional)
Los parámetros configurables incluyen:
- **max_new_tokens**: Número máximo de tokens generados.
- **temperature**: Controla la diversidad de la generación.
- **min_new_tokens**: Número mínimo de tokens generados.

## Referencias

A continuación, se enumeran las principales fuentes y referencias bibliográficas utilizadas en este proyecto:

1. [Documentación de Transformers - Hugging Face](https://huggingface.co/docs/transformers/en/index): Recurso oficial para comprender el uso y funcionalidades de la biblioteca Transformers.
2. [Modelos LLaMA - Meta](https://huggingface.co/collections/meta-llama/llama-32-66f448ffc8c32f949b04c8cf): Colección oficial de modelos LLaMA en Hugging Face.
3. [Quantization en LLM - Tech Research Space](https://medium.com/@techresearchspace/what-is-quantization-in-llm-01ba61968a51): Explicación detallada sobre la cuantización y su impacto en modelos de lenguaje.
4. [Chain of Thought Prompting - Deepgram](https://deepgram.com/learn/chain-of-thought-prompting-guide): Guía sobre la técnica de Chain of Thought Prompting para mejorar la precisión de LLMs.
5. [Few-shot Prompting - Learn Prompting](https://learnprompting.org/docs/basics/few_shot?srsltid=AfmBOopY1hz1ELtbvzCDem35nexC4X8LwZImQlWRuWQ2f1k8YcqNk3u_): Introducción al uso de Few-shot Prompting para personalizar respuestas de modelos de lenguaje.


