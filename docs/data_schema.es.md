# Estructura de datos

Convención de ingeniería de datos por capas

![ingeniería de datos por capas](https://docs.kedro.org/en/stable/_images/data_layers.png)

| `Carpeta en data` | `Descripción` |
| ---------------------- | --- |
| `raw`            | inicio del pipeline, contiene el/los modelo(s) de datos de origen que nunca deben ser modificados, forman tu única fuente de verdad. Estos modelos de datos típicamente no tienen tipo en la mayoría de los casos, ej. csv, pero esto varía de caso a caso |
| `intermediate`   | modelo(s) de datos opcionales, que se introducen para tipar tu(s) modelo(s) de datos crudos, ej. convirtiendo valores basados en cadenas de texto a su representación tipada actual |
| `primary`        | modelo(s) de datos específicos del dominio que contienen datos limpiados, transformados y procesados desde raw o intermediate, que forman la capa de entrada para tu ingeniería de características |
| `feature`        | modelo(s) de datos específicos de análisis que contienen un conjunto de características definidas contra los datos primarios, agrupados por área de análisis y almacenados contra una dimensión común |
| `model input`    | modelo(s) de datos específicos de análisis que contienen todos los datos de características contra una dimensión común y, en el caso de proyectos en producción, contra una fecha de ejecución de análisis para asegurar el seguimiento de cambios históricos de las características a lo largo del tiempo |
| `models`         | modelos de aprendizaje automático pre-entrenados almacenados y serializados |
| `model output`   | modelo(s) de datos específicos de análisis que contienen los resultados generados por el modelo basados en los datos de entrada del modelo |
| `reporting`      | modelo(s) de datos de reportes que se usan para combinar un conjunto de datos primarios, características, entrada del modelo y salida del modelo usados para construir el dashboard y las vistas. Encapsula y elimina la necesidad de definir cualquier mezcla o unión de datos, mejora el rendimiento y el reemplazo de la capa de presentación sin tener que redefinir los modelos de datos |

## Referencias

- <https://docs.kedro.org/en/stable/faq/faq.html#what-is-data-engineering-convention>
- <https://towardsdatascience.com/the-importance-of-layered-thinking-in-data-engineering-a09f685edc71>
