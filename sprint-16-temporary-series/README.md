# Proyecto: Sweet Lift Taxi

## Descripción del proyecto

La compañía Sweet Lift Taxi ha recopilado datos históricos sobre pedidos de taxis en los aeropuertos. Para atraer a más conductores durante las horas pico, necesitamos predecir la cantidad de pedidos de taxis para la próxima hora. Construye un modelo para dicha predicción.

La métrica RECM en el conjunto de prueba no debe ser superior a 48.

## Instrucciones del proyecto

1. Descarga los datos y remuestréalos de tal forma que cada punto de datos de los datos originales caigan dentro de intervalos de una hora.
2. Analiza los datos.
3. Entrena diferentes modelos con diferentes hiperparámetros. La muestra de prueba debe ser el 10% del conjunto de datos inicial.
4. Prueba los datos usando la muestra de prueba y proporciona una conclusión.

## Descripción de datos

Los datos se almacenan en el archivo `/datasets/taxi.csv`. [Descarga el conjunto de datos](https://practicum-content.s3.us-west-1.amazonaws.com/datasets/taxi.csv?etag=11687de0e23962e5a11c9d8ae13eb630)

El número de pedidos está en la columna `num_orders`.

## Evaluación del proyecto

Hemos definido los criterios de evaluación para el proyecto. Léelos con atención antes de pasar al ejercicio.

Esto es en lo que se fijarán los revisores al examinar tu proyecto:

- ¿Seguiste todos los pasos de las instrucciones?
- ¿Cómo preparaste los datos?
- ¿Qué modelos e hiperparámetros consideraste?
- ¿Conseguiste evitar la duplicación del código?
- ¿Cuáles fueron tus hallazgos?
- ¿Mantuviste la estructura del proyecto?
- ¿Mantuviste el código limpio?

## Temas del sprint que se aplican

- Graficación de series temporales
- Remuestreo
- Tendencia y estacionalidad
- Series estacionarias
- Pronóstico de series temporales
- Exactitud del pronóstico en series temporales
- Entrenamiento de modelos de predicción de series temporales
