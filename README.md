<h1 align="center"> Sistema de recomendación </h1>


<p align="center">
  <img src="./imagen/steam.png" alt="STEAM" width="400">
</p>


<h1 align="center"> Desarrollo del Sistema de Recomendación para STEAM </h1>

## Contexto

Como parte de mi formación como Cientista de Datos, elaboré este primer proyecto, simulando un entorno real de trabajo, que consistió en la elaboración de un Modelo de Recomendación de videojuegos para la plataforma STEAM, con el objetivo de que ésta permita mejorar la experiencia de sus usuarios.

## Descripción del proyecto:

- El objetivo principal es desplegar una producto mínimo viable (MVP) de una API que le permita a los departamentos de Analytics y Machine Learning de la empresa STEAM realizar 5 consulta específicas relacionadas con los datos de sus usuarios y plataforma, además del modelo de recomendación de videojuegos, basado en un modelo ítem-ítem.


## Fases del Proyecto

Las etapas de este proyecto se resumen a continuación: 

- Extracción, Transformación y Carga (ETL): Proceso de carga de datos y tratamiento preliminar para su adecuado consumo. 

- Análisis Exploratorio de Datos (EDA): Investigar loas relaciones que hay entre las variables del dataset, y detectar patrones. 

- Funciones para el funcionamiento de la API: Implementación de las 5 funciones solicitadas con el objetivo de disponibilizar estas consultas al personal de la empresa.

- Sistema de recomendación: Desarrollo de un modelo de Machine Learning cuyo objetivo es recomendar a los usuarios juegos similares a los que consume.

- Implementación de la API y despliegue: Se utiliza RENDER para disponibilizar este MVP de forma online.

- A continuación se detalla cada una de las etapas.

## ETL (Extracción, Transformación y Carga)

La etapa de extracción de datos y su transformación fue la etapa más desafiante y que tomó mayor tiempo de trabajo, debido a que los datos no venían listos para empezar a procesarlos. Las tareas realizadas consisteron en identificar la forma correcta para leer los archivos, desanidado de columnas, análisis de las bases de datos para su preproceso, eliminación de columnas innecesarias para nuestro análisis, ajuste de tipos de datos, tratamiento y análisis preliminar de datos faltantes y nulos y limpieza. En esta etapa también se realizó el análisis de sentimiento sobre la columna de comentarios que dejan los usuarios de la plataforma, aplicando los porcesos de  SentimentIntensityAnalyzer(), PorterStemmer() y  WordNetLemmatizer().  


## EDA (Análisis Exploratorio de Datos)
En esta etapa se realizó un análisis profundo de las tres bases de datos con las que trabajamos con la finalidad de identificar información relevante de los datasets, e identificar patrones que nos entregaran mayor comprensión del negocio. Esta tarea implicó primero, realizar un an´´alisis estadístico de la información, realizar tratamiento de elementos duplicados, datos faltantes y nulos, identificadno por ejemplo, que existían patrones claros del porqué de la información faltante en algunos casos. En esta primera parte, la estrategia utilizada para el tratamiento de valores faltantes fue utilizar una nueva base de datos de STEAM y completar los valores que nos faltaban, y de esta forma, evitar la pérdida de información relevante. Una vez desarrolladas estas estrategias, se realizaron representaciones gráficas con el objetivo de obtener una comprensión más profunda y visual de la naturaleza de los datos y de las características del negocio. Este proceso permitió identificar ciertos patrones, tendencias y particularidades esenciales, brindando así una base sólida para la siguiente etapa de desarrollo del proyecto.


## Construcción de la API

Para el desarrollo de la API, se utilizó el framework FASTAPI. Las funciones creadas para los endpoints que serán consumidos en la API son:

1. developer(desarrollador: str): Cantidad de items y porcentaje de contendio FrEE por año segun empresa desarrolladora.

2. userdata(user_id: str): Deve devolver cantidad de dinero gastado  por el usuario, el procentaje de recomendación en base a reviews.recommend y cantidad de items.

3. UserForGenre(genero: str): La función UserForGenre devuelve el usuario que acumula la mayor cantidad de horas jugadas para el género especificado, junto con una lista que muestra la acumulación de horas jugadas por año.

4. best_developer_year(año: int): Devuelve el top 3 de de desarrolladores con juegos más recomendados por usuarios para el año dado.

5. developer_reviews_analysis(desarrollador: str): egún la empresa desarrolladora, se devuelve un diccionario con el nombre de la desarrolladora como llave y una lista con la cantidad total 
    de registros de reseñas de usuarios que se encuentren categorizados con un análisis de sentimiento como valor. 

## Modelamiento (Machine Learning)

En esta etapa e llevó a cabo el modelado para el desarrollo del Sistema de Recomendación, basado en la similitud del coseno, para lo cual se creó la función item-item, que recibe como input el id del juego y devuelve juegos recomendados similares.
- Primera Función item-item, introduzco el id del juego y me devuelve juegos recomendados.


## Render/Deploy

En esta fase se utilizó la plataforma [RENDER](https://www.render.com) para disponibilizar nuestra API en línea.

Link al MPV:  [Deploy/link](https://deploy-9w66.onrender.com)


## Video Explicativo

En este apartado, dejo disponible el video explicativo del MVP de este proyecto.

