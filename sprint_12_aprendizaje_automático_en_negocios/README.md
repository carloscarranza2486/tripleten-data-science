# OilyGiant: predicción de reservas y análisis de riesgo para pozos petrolíferos

## Descripción del proyecto

Proyecto desarrollado para la compañía de extracción de petróleo OilyGiant. El objetivo es determinar en cuál de tres regiones conviene abrir 200 pozos nuevos, maximizando el beneficio esperado y manteniendo el riesgo de pérdidas por debajo del 2.5 %.

Se entrena un modelo de regresión lineal que predice el volumen de reservas de un pozo a partir de sus datos geológicos, se seleccionan los pozos más prometedores de cada región y se estima la distribución de beneficios con la técnica de bootstrapping.

## Condiciones del negocio

- **Presupuesto de inversión:** 100 millones de dólares para el desarrollo de 200 pozos.
- **Ingreso por unidad:** un barril genera 4.5 USD. El ingreso por unidad de producto (miles de barriles) es de 4 500 USD.
- **Exploración:** se evalúan 500 puntos por región, de los cuales se seleccionan los 200 mejores.
- **Tolerancia al riesgo:** solo se aprueban las regiones con riesgo de pérdidas inferior al 2.5 %. Entre las que cumplan, se elige la de mayor beneficio promedio.
- **Modelo predictivo:** restringido exclusivamente a regresión lineal.

## Descripción de los datos

Tres conjuntos de datos sintéticos de exploración geológica, uno por región: `geo_data_0.csv`, `geo_data_1.csv` y `geo_data_2.csv`, con 100 000 pozos cada uno.

- `id`: identificador del pozo.
- `f0`, `f1`, `f2`: tres características geológicas del punto.
- `product`: volumen de reservas en miles de barriles (variable objetivo).

## Etapas del proyecto

1. **Carga y preparación de los datos.** Revisión de calidad, tipos y distribuciones de las tres regiones.
2. **Entrenamiento y prueba del modelo.** División 75:25, regresión lineal por región, volumen medio predicho y RMSE.
3. **Preparación del cálculo de ganancias.** Constantes del negocio y volumen mínimo por pozo que evita pérdidas.
4. **Cálculo del beneficio.** Función de beneficio sobre los 200 pozos con mayor predicción en cada región.
5. **Evaluación de riesgos con bootstrapping.** 1 000 submuestras de 500 puntos, beneficio promedio, intervalo de confianza del 95 % y riesgo de pérdidas.

## Resultados

El volumen de equilibrio es de 111.11 miles de barriles por pozo, un umbral que ninguna región alcanza en promedio (92.50, 68.83 y 95.00), de modo que el negocio depende por completo de la selección de pozos.

Con los 200 mejores pozos de cada región, el bootstrapping arroja:

| Región | Beneficio medio | Intervalo de confianza 95 % | Riesgo de pérdidas |
| --- | --- | --- | --- |
| Región 0 | 3 961 650 USD | [-1 112 155 , 9 097 669] | 6.9 % |
| Región 1 | 4 560 451 USD | [338 205 , 8 522 895] | 1.5 % |
| Región 2 | 4 044 039 USD | [-1 633 504 , 9 503 596] | 7.6 % |

**Región recomendada: la región 1.** Es la única que cumple el límite de riesgo del 2.5 % y, entre las aprobadas, la de mayor beneficio esperado. Su intervalo de confianza es además el único que queda por completo en terreno positivo.

El resultado es contraintuitivo: la región 1 tiene el volumen medio de reservas más bajo, pero su modelo predice con un RMSE de 0.89 frente a 37.58 y 40.03 de las otras dos. Al elegir solo 200 pozos entre 500 puntos explorados, esa precisión pesa más que el volumen disponible.

## Tecnologías utilizadas

- **Lenguaje:** Python 3
- **Análisis de datos:** pandas, NumPy
- **Visualización:** Matplotlib
- **Machine learning:** scikit-learn (`LinearRegression`, `train_test_split`, `mean_squared_error`)
- **Estadística:** bootstrapping con `numpy.random.RandomState`

## Cómo ejecutar el proyecto

Abre `notebook.ipynb` con Jupyter, VS Code o Cursor y ejecuta las celdas en orden.

El notebook carga los datos con un `try/except` que funciona en los dos entornos: busca los CSV junto al notebook y, si no los encuentra, los toma de la ruta `/datasets/` que usa la plataforma de TripleTen. No hace falta ajustar rutas.

Se necesitan `pandas`, `numpy`, `matplotlib` y `scikit-learn` en el entorno activo.
