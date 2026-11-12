# Estructura del sprint final

¡Bienvenido al Proyecto Final del Bootcamp de Data Scientist!

Has recorrido un largo camino desde las bases de Python y la manipulación de datos, hasta el entrenamiento de modelos predictivos y el entendimiento de métricas de negocio. Este proyecto final ha sido diseñado como una simulación realista de lo que enfrentarás en la industria.

El objetivo de esta etapa es que demuestres tu capacidad para integrar habilidades técnicas —como la limpieza de datos, el análisis exploratorio y el modelado predictivo— con habilidades estratégicas, traduciendo tus hallazgos de código en recomendaciones de negocio claras y fundamentadas.

En el mundo real, los científicos de datos no trabajan aislados. Durante este proyecto, contarás con un equipo para garantizar tu éxito:

- **Tú (El Científico de Datos):** Eres el dueño del proyecto. Tu responsabilidad es proponer, justificar y documentar cada decisión metodológica. Esperamos de ti un código limpio, reproducible y, sobre todo, un análisis que cuente una historia coherente.
- **El Revisor (Validación Técnica):** Actuará como tu líder técnico. Evaluará tu entrega basándose en métricas estrictas y la viabilidad de tus conclusiones. Si tu modelo no alcanza el estándar o tu código presenta fallos, te solicitará iteraciones. Su objetivo es asegurar que tu trabajo tenga calidad profesional.
- **Tu Tutor (Consultoría Senior):** Será tu mentor durante el proceso. Utiliza las sesiones 1:1 para intercambiar ideas, debatir estrategias de modelado o destrabar obstáculos técnicos. No te dará las respuestas, pero te guiará hacia las mejores prácticas.
- **Success Manager (Gestión y Soporte):** Será tu facilitador operativo. Acude a esta figura para resolver cualquier necesidad administrativa, dudas sobre cronogramas o problemas de acceso que puedan frenar tu avance.

Para que tu proyecto sea aprobado, te sugerimos adoptar la mentalidad de un analista senior, guiándote por los siguientes principios:

1. **Valoramos el pragmatismo:** Un modelo simple y bien justificado siempre será superior a un modelo complejo que no logras explicar. Quienes tomarán decisiones basándose en tu trabajo necesitan claridad, no necesariamente el algoritmo más sofisticado.
2. **Tú eres el responsable del código:** Eres libre de utilizar herramientas de inteligencia artificial como apoyo durante tu desarrollo. Sin embargo, asegúrate de comprender cada línea de código que decidas incluir. Ante el revisor, tú eres el único autor y responsable de tus resultados.
3. **Los datos deben contar una historia:** No utilices las celdas de texto de tu entorno de trabajo (Jupyter Notebook) únicamente para narrar lo obvio (por ejemplo, "Aquí concateno dos tablas"). Úsalas para explicar el porqué de tus decisiones estratégicas y cómo estas impactan el objetivo final.

Tienes las herramientas, el conocimiento y el equipo de apoyo. Revisa a continuación el documento con el contexto de negocio de tu caso asignado y comienza a trazar tu plan.

¡Mucho éxito!

---

# Caso de negocio: Retención de Clientes en Interconnect

## Contexto

El operador de telecomunicaciones Interconnect se enfrenta a un desafío crítico: una tasa de cancelación de clientes (Churn) cada vez mayor. El equipo de marketing sabe que retener a un cliente actual es mucho más barato que adquirir uno nuevo. Por ello, quieren implementar un sistema proactivo: si descubrimos a tiempo que un usuario planea irse, se le ofrecerán códigos promocionales y opciones de planes especiales para retenerlo.

El problema es que actualmente no saben a quién ofrecerle estas promociones. Aquí es donde entras tú como Científico de Datos.

Tu objetivo es desarrollar un modelo predictivo que responda a la siguiente pregunta: **¿Este cliente se dará de baja pronto (Sí o No)?**

Para desarrollar tu modelo, el equipo de ingeniería de datos ha recopilado el siguiente historial sobre los clientes de la compañía.

## Descripción de los Datos

Los datos están divididos en cuatro archivos:

- `contract.csv`: Información del contrato (tipo de facturación, método de pago, fechas de inicio y fin).
- `personal.csv`: Datos demográficos del cliente.
- `internet.csv`: Información sobre los servicios de Internet contratados (fibra óptica, DSL, antivirus, etc.).
- `phone.csv`: Información sobre los servicios telefónicos (líneas múltiples).

Para acceder a los datos dentro de la plataforma, usa la ruta `/datasets/final_provider/`.  En este entorno, están en la carpeta sprint-19-final-project

## Consideraciones

Interconnect ofrece servicios separados. Algunos clientes solo tienen teléfono, otros solo internet, y otros ambos. Cuando unas las tablas, es normal y esperado que se generen valores nulos (`NaN`) en los servicios que un cliente no contrató. Piensa cómo debes rellenar esos valores nulos para que el modelo entienda que significan la "ausencia de un servicio" y no un error en los datos.

Por otro lado, no encontrarás una columna explícita que se llame "Fuga" o "Churn". Deberás inferir el estado actual del cliente analizando la fecha en la que finalizó su contrato (`EndDate`).

- Si un contrato tiene una fecha de finalización concreta, sabemos qué ocurrió con ese cliente.
- Si en lugar de una fecha dice `"No"`, significa que la historia del cliente con nosotros aún continúa.

Deberás usar esta lógica para crear tu variable objetivo.