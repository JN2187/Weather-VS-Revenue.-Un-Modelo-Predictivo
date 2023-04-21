# Proyecto de análisis de datos: ¿Está la audiencia de mi medio relacionada con la inestabilidad climática?

En este proyecto de análisis de datos, se ha llevado a cabo una investigación para demostrar la hipótesis de que la audiencia de un medio de comunicación está vinculada a la inestabilidad climática, en concreto a las precipitaciones. La hipótesis se basa en la intuición de que cuando llueve, la gente tiende a pasar más tiempo en interiores y, por lo tanto, aumenta la audiencia de los medios de comunicación.

Para llevar a cabo esta investigación, se han utilizado tres fuentes de datos diferentes. En primer lugar, se ha utilizado la API de Google Analytics para obtener datos sobre la audiencia del medio de comunicación a lo largo de todo el año 2022. Se ha generado un dataframe con la audiencia media diaria y mensualizada del site, con el objetivo de analizar si se producen picos de audiencia cuando llueve.

En segundo lugar, se han utilizado datos de precipitaciones medias tanto diarias como mensuales de cada una de las estaciones meteorológicas de España en el año 2022, excluyendo a Canarias para no desvirtuar el dato de lluvia de la península. Se ha definido qué es lluvia a partir de los datos de las precipitaciones, teniendo en cuenta que los datos vienen en mm3, y considerando lluvia a partir de 2,5mm3 de media en España.

Por último, se han utilizado datos de revenue, clientes, impresiones, formatos, tipos de transacciones, tipos de dispositivos e industria de todo el año 2022 generados por el site. Se han limpiado y filtrado los datos para quedarse con los clientes de mayor facturación y, a continuación, se han mergeado los datos de revenue, audiencia media y precipitaciones.

Para analizar los datos y hacer predicciones del revenue, se ha utilizado un modelo de H2OAutoML. Se ha cargado el dataframe con todos los datos y se ha cargado en un modelo de H20Frame.

En la carpeta del repositorio denominada data se encuentran almacenados todos los archivos generados en los notebooks mencionados. Este proyecto es un ejemplo de cómo se puede utilizar el análisis de datos para buscar relaciones entre variables y encontrar patrones que permitan mejorar el rendimiento de un medio de comunicación.

## Contenido

1. [Repositorio de Carpetas](#repositorio-de-carpetas)
2. [Librerías](#librerías)
3. [Next Steps](#next-steps)

## Repositorio de Carpetas

- **data**: Carpeta que contiene los archivos de datos utilizados en los notebooks. Incluye archivos .txt de Adomik, archivos .csv de Weather y archivos generados del mergeo de todos los datos.

- **notebooks**:

- **GA_API.ipynb**: Notebook que utiliza la API de Google Analytics para obtener la audiencia media diaria y mensual de un sitio web durante todo el año 2022.

- **Weather.ipynb**: Notebook que utiliza datos de precipitaciones de las estaciones meteorológicas de España para obtener la lluvia media diaria y mensual en la península durante todo el año 2022.

- **Adomik.ipynb**: Notebook que utiliza datos de facturación y clientes de un sitio web para obtener información sobre los clientes con mayor facturación durante todo el año 2022.

- **H20.ipynb**: Notebook que utiliza el marco de trabajo H2O para generar un modelo de aprendizaje automático que pueda predecir el revenue en función de los datos de audiencia y precipitaciones.

- **Streamlit**: Todo el código necesario para cargar toda la información en un .py, llamado Streamlit.py,

## Librerías

### GA_API.ipynb y Weather.ipynb

- numpy
- pandas
- seaborn
- matplotlib
- googleapiclient
- service_account
- ServiceAccountCredentials
- dotenv

### Adomik.ipynb

- pandas
- numpy
- datetime
- random
- string
- locale
- dotenv
- seaborn
- matplotlib
- statsmodels

### H20.ipynb

- pandas
- h2o
- H2OAutoML

## Next Steps

La idea de éste proyecto es poder implementar los resultados obtenido para tener un uso real y mejorar el revenue de la parte de la venta programática de mi compañía.