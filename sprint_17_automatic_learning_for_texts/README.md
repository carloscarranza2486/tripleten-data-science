# Sprint 17: Aprendizaje automático para textos

## Descripción del proyecto

Film Junky Union, una nueva comunidad vanguardista para los aficionados de las películas clásicas, está desarrollando un sistema para filtrar y categorizar reseñas de películas. El objetivo es entrenar un modelo para detectar las críticas negativas de forma automática. Para lograrlo, se utiliza un conjunto de datos de reseñas de películas de IMDB con etiquetado, para construir un modelo que clasifique las reseñas como positivas y negativas. Este deberá alcanzar un valor F1 de al menos 0.85.

## Instrucciones del proyecto

1. Carga los datos.
2. Preprocesa los datos, si es necesario.
3. Realiza un análisis exploratorio de datos y haz tu conclusión sobre el desequilibrio de clases.
4. Realiza el preprocesamiento de datos para el modelado.
5. Entrena al menos tres modelos diferentes para el conjunto de datos de entrenamiento.
6. Prueba los modelos para el conjunto de datos de prueba.
7. Escribe algunas reseñas y clasifícalas con todos los modelos.
8. Busca las diferencias entre los resultados de las pruebas de los modelos en los dos puntos anteriores. Intenta explicarlas.
9. Muestra tus hallazgos.

La plantilla del proyecto ya contiene algunos fragmentos de código que se pueden usar o eliminar:

- un poco de análisis exploratorio de datos con algunos gráficos;
- `evaluate_model()`: una rutina para evaluar un modelo de clasificación que se ajusta a la interfaz de predicción de scikit-learn;
- `BERT_text_to_embeddings()`: una ruta para convertir lista de textos en insertados con BERT.

El trabajo principal es construir y evaluar modelos. La plantilla sugiere probar modelos de clasificación basados en regresión logística y potenciación del gradiente, pero se pueden probar otros métodos.

No es obligatorio usar BERT, porque requiere mucha potencia computacional y es muy lento en CPU para el conjunto de datos completo. Se puede incluir BERT para una parte del conjunto de datos, de manera local y tomando solo un par de cientos de objetos por cada parte (entrenamiento/prueba). Si se usa BERT, hay que indicarlo en la primera celda (el encabezado del proyecto).

## Descripción de los datos

Los datos se almacenan en el archivo `imdb_reviews.tsv`. Fueron proporcionados por Andrew L. Maas, Raymond E. Daly, Peter T. Pham, Dan Huang, Andrew Y. Ng, y Christopher Potts. (2011). Learning Word Vectors for Sentiment Analysis. La Reunión Anual 49 de la Asociación de Lingüística Computacional (ACL 2011).

Campos seleccionados:

- `review`: el texto de la reseña
- `pos`: el objetivo, '0' para negativo y '1' para positivo
- `ds_part`: 'entrenamiento'/'prueba' para la parte de entrenamiento/prueba del conjunto de datos, respectivamente

Hay otros campos en el conjunto de datos, que se pueden explorar si se desea.

## Evaluación del proyecto

- Cargaste y preprocesaste los datos de texto para su vectorización.
- Transformaste los datos de texto en vectores.
- Definiste, entrenaste y probaste los modelos.
- Se alcanzó el umbral de la métrica (F1 >= 0.85).
- Colocaste todas las celdas de código en el orden de su ejecución.
- Puedes ejecutar sin errores todas las celdas de código.
- Sacaste conclusiones.

Calidad general del proyecto:

- ¿Mantuviste la estructura del proyecto?
- ¿Mantuviste limpio tu código?
- ¿Conseguiste evitar la duplicación del código?
- ¿Cuáles fueron tus hallazgos?
