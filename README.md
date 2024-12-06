# Resumen Automático de Fallos Judiciales con LLMs

## Introducción
En el Boletín Judicial de los Tribunales Provinciales de Córdoba, un equipo liderado por la Dra. Valeria Sola trabaja en la extracción de metadatos, redacción de síntesis y elaboración de sumarios de fallos judiciales. Estas tareas se realizan manualmente sobre textos denominados [Fallos](https://drive.google.com/file/d/1M7qSGdbUqznr94c2qDan3uIS5SkR5TiE/view?usp=sharing), generando como resultado documentos denominados [Sumarios](https://drive.google.com/file/d/1yk6CjVThjc6iFP7Dw3XlPv6srfCkQhDi/view?usp=sharing). El objetivo es ofrecer documentos estandarizados que resumen causas legales en los fueros Civil y Penal, siguiendo las [Normas de estilo para la redacción de sumarios de jurisprudencia](https://drive.google.com/file/d/18NEBdtVR5UuGBziGEfFb1CA8ePUUsOnd/view?usp=sharing).

Este proceso manual es altamente demandante y consume tiempo que los abogados podrían dedicar a tareas más interpretativas. Este proyecto propone una herramienta automática que genere textos preliminares, permitiendo a los abogados centrarse en la validación, profundización y edición de los documentos generados, optimizando su esfuerzo y asegurando el cumplimiento de los estándares establecidos.

## Hipótesis y Objetivos Iniciales

La **hipótesis** sobre la que trabajamos desde el principio fue que podríamos generar **resúmenes útiles** para los abogados, tales que les ahorren una cantidad considerable de tiempo, solo usando **prompt engineering**, sin la necesidad de **fine-tunear** algún modelo.



## Resultados Finales

Los resultados obtenidos con el modelo **Llama3.2-11B-Visual-Instruct** en configuración de 16 bits se resumen en la siguiente tabla:

![Desempeño del Modelo Llama3.2-11B-Visual-Instruct 16 bit](llama3_2_performance.png)

El modelo demostró un desempeño excelente en las tareas de extracción de metadatos y redacción de síntesis, alcanzando un 100% de buen formato y cohesión/coherencia. En la tarea de generación de sumarios, también obtuvo un desempeño destacado con un 96% de buen formato y cohesión/coherencia, aunque un 4% presentó problemas menores de formato y cohesión. El tiempo total de procesamiento fue de 31 minutos.


## Planificación y Ejecución

El desarrollo de este proyecto implicó un proceso iterativo de aprendizaje y experimentación con diversos entornos y modelos hasta alcanzar la solución final. A continuación, se detalla esta trayectoria.

### Familiarización con los Modelos
En una primera instancia, se utilizó la plataforma **Google Colab** para comprender el manejo de modelos de lenguaje. Durante esta etapa inicial, el enfoque estuvo en:
- Cargar y utilizar modelos preentrenados.
- Experimentar con bibliotecas especializadas como **Transformers**, **Accelerate** y **Torch**.
Aprovechando los 15 GB de GPU de la versión gratuita de Colab, fue posible realizar pruebas básicas y obtener los primeros resultados.

### Acceso a Recursos de Alto Desempeño
En la segunda fase, se accedió a servidores avanzados en San Francisco, Córdoba, equipados con dos **NVIDIA A30** de 25 GB de GPU cada una. Este entorno permitió:
- Cargar un modelo **LLaMA de 8B parámetros**.
- Obtener resultados prometedores y eficientes en la extracción de metadatos y la generación de síntesis.

### Decisiones Estratégicas: Selección del Modelo
Tras un análisis exhaustivo de los pros y contras de varios modelos, se decidió trabajar con modelos de la familia **LLaMA**, destacando las siguientes decisiones:
- No utilizar modelos con tareas predefinidas, como **LLaMA3.1 8B Instruct-Summarization**, que inicialmente parecía una opción viable pero ofrecía menor flexibilidad.
- Priorizar modelos **Instruct-based**, los cuales permitieron una mayor adaptabilidad y personalización en la generación de texto.

Este enfoque iterativo y basado en decisiones estratégicas fue clave para lograr un balance entre desempeño, flexibilidad y recursos computacionales disponibles.


## Librerías y Codebases
- **[Transformers](https://huggingface.co/docs/transformers/)**: Biblioteca para trabajar con modelos de lenguaje preentrenados.
- **[Python](https://www.python.org/)**: Lenguaje de programación principal.
- **[CUDA](https://developer.nvidia.com/cuda-toolkit)**: Para la aceleración en GPU.
- **[Torch](https://pytorch.org/)**: Framework para machine learning.
- **[Modelo Llama-3.2-11B-Vision-Instruct](https://github.com/facebookresearch/llama)**: Modelo preentrenado especializado.

## Feedback e Integración de Sugerencias
- **Comentarios Recibidos:** Resume las devoluciones de los otros dos grupos.
- **Implementación de Sugerencias:** Explica qué sugerencias se integraron y cuáles no, justificando estas decisiones.

## Metodología
- **Preprocesamiento:** Detalla cómo se procesaron los datos de entrada.
- **Arquitectura del Modelo:** Describe brevemente el modelo LLM utilizado y los ajustes realizados.
- **Entrenamiento/Inferencia:** Explica cómo se configuraron y ejecutaron estos procesos.

## Resultados
- **Métricas:** Presenta las métricas de evaluación utilizadas y los valores obtenidos.
- **Visualizaciones:** Incluye gráficos o tablas relevantes que respalden los resultados.

## Conclusiones y Trabajo Futuro
- Discute los aprendizajes clave del proyecto.
- Propón posibles mejoras o extensiones para futuros trabajos.

## Requisitos del Proyecto
Lista dependencias necesarias para ejecutar el proyecto.

## Uso
Instrucciones paso a paso para replicar o ejecutar el proyecto.

## Referencias
Incluye todas las citas y referencias bibliográficas usadas.

