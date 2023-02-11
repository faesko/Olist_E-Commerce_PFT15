<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> PROYECTO FINAL </h1>

##### - [ANGEL ZAVALETA](https://github.com/AngelZavaleta)
##### - [JOSÉ ACEVEDO](https://github.com/JoseAcevedo6)
##### - [LEONARDO CUETO](https://github.com/Leonardo1278)
##### - [NICOLÁS LIRA](https://github.com/faesko/)

# <h1 align=center>**`OLIST`**</h1>

<p align=center><img src="https://eminence.ch/wp-content/uploads/2022/02/commerce-tips-2022.jpg" alt="Image" height="300" width="750" /><p>

## Introducción

Business Intelligence (BI) es un tipo de software que se alimenta de datos de negocios y presenta reportes, paneles, tablas y gráficos de forma amigable para el usuario. Las herramientas de BI permiten a los usuarios de negocio acceder a diferentes tipos de datos: históricos y actuales, de terceros e internos, así como datos semiestructurados y datos no estructurados como las redes sociales. Los usuarios pueden analizar esta información para obtener insights sobre el rendimiento del negocio.

Según la revista CIO: "Aunque la BI no les dice a los usuarios empresariales qué hacer o qué sucederá si toman un determinado curso, la BI tampoco se trata únicamente de generar informes. Más bien, BI ofrece una forma para que las personas examinen los datos para comprender las tendencias y canalizar los insights".

Las organizaciones pueden utilizar la información obtenida de BI y el análisis de datos para mejorar las decisiones comerciales, identificar problemas, detectar tendencias del mercado y encontrar nuevos ingresos u oportunidades comerciales.

## Propuesta de trabajo

En 2021, la venta minorista de productos a través de e-commerce significó un saldo aproximado de 5.2 trillones de dólares en todo el mundo y se infiere que dicha cifra aumentará un 56% en los próximos años, llegando a los 8.1 trillones en 2026.

Olist es una compañía brasileña prestadora de servicio E-commerce para PYMES que funciona como un marketplace, es decir, funciona como “tienda de tiendas” donde diferentes vendedores pueden ofrecer sus productos a consumidores finales.

## Rol a desarrollar

Con el objetivo primordial de seguir conectando a pequeñas empresas (PYMES) con mercados más grandes y mejorar la experiencia del usuario, SLG-Bi Analitics se enfoca en encontrar soluciones innovadoras que permitan a sus usuarios vender sus productos a un mayor número de clientes.
Para lograrlo, se analizaron los datos de Olist de 2016 a 2018, con lo que se busca entregar un MVP (minimum viable product).

## Entendimiento de la situación actual

El E-commerce se refiere a la compra y venta de bienes o servicios a través de Internet. Ha crecido rápidamente en los últimos años y es ahora una parte importante de la economía mundial. El E-commerce permite a las empresas alcanzar una base de clientes más amplia y ofrece comodidad para los compradores. Además, también puede tener un menor costo operativo en comparación con una tienda física, lo que lo hace particularmente atractivo para las pequeñas empresas. Una de las formas más comunes de comercio electrónico es el comercio minorista en línea, que incluye sitios web de compras como Amazon, Alibaba, Mercadolibre, Olist, entre otros.

Una de las principales ventajas del E-commerce es la capacidad de recopilar datos sobre el comportamiento, las preferencias y los hábitos de compra de los clientes, lo que ayuda a las empresas a tomar decisiones basadas en datos y mejorar sus ofertas con el tiempo. Además, el E-commerce también proporciona una herramienta valiosa para las empresas para llegar a los clientes con el comercio transfronterizo, lo que era difícil antes de Internet.

Sin embargo, el E-commerce tiene algunos inconvenientes, como el potencial de fraude y la dificultad de construir confianza con los clientes en línea. También requiere una logística, un servicio de pago y un servicio al cliente eficiente para operar, lo que puede ser desafiante para algunas empresas manejar por sí mismas.


## Objetivos específicos del trabajo y del grupo

KPI 1: Con respecto a los MQLs, analizar cómo la venta de los nuevos "MQLs (vendedores)" afectaría el ingreso de Olist.
- Objetivo: Reducir el tiempo de ingreso (aceptación) de los clientes potenciales a Olist, para aumentar sus ganancias.

KPI 2: Calcular la variación porcentual de ventas por "categoría de productos" (por trimestre).
- Objetivo: Identificar las tendencias de ventas por categorías de productos a través del tiempo, ayudando a Olist a descubrir oportunidades comerciales por temporada.

KPI 3: Identificar los 5~10 productos más vendidos y los más populares por trimestre y por estado.
- Objetivo: Establecer un ranking de productos con mejor score basado en el indice de popularidad, logrando posicionar los productos que generen mayor rentabilidad.

## Alcance y fuera de alcance

#### Motivación del proyecto
- Ayudar a mejorar el proceso de ventas a través de un análisis de negocios basado en KPI’s para proponer a nuestro cliente (Olist) opciones de mejora en sus servicios como E-Commerce.

#### Objetivos 
- Verificar la calidad de los datos y proceder con ETL.
- Implementar Data Warehouse como modelo de base de datos.
- Presentar un Dashboard con indicadores de desempeño. 
- Crear una aplicación para predecir los productos en tendencia basada en un modelo de ML.

#### Supuestos
- Datasets que brindan información confiable para proyección y análisis de datos.
- Tiempo suficiente para término de proyecto.
- Disponibilidad de tiempo por parte del equipo.
- Los integrantes del equipo permanezcan hasta la culminación del proyecto.

#### Restricciones 
- Se debe culminar el proyecto en 3 semanas.
- Equipo de trabajo con mínimo 4 integrantes.
- Contar con los perfiles de Data Science asumiendo los roles de Analista e Ingeniero de Datos.

#### Exclusiones
- Un Dashboard, mediante el software Power BI y presentación con Streamlit.
- DataWarehouse con respaldo en GitHub, diseñado con SQLAlchemy y SQLite.
- Metodología híbrida: metodología ágil combinado con la pauta entregada por soyHenry. 
- Uso de Trello como herramienta para gestión de proyectos.

#### Criterios de Aceptación
- El dashboard debe ser funcional y entendible.
- Una base de datos sólida.
- EDA de calidad en los entregables.

## Solución propuesta 

#### 1. Stack tecnologico

<img src="/src/stack_tecno.png" alt="Image" />

	Python, Pandas, Numpy, SQLalchemy, Power BI, SQLite, Streamlit, Tkinter, Sklearn

#### 2. Metodología de trabajo:

Metodología híbrida: 

- Metodología ágil

<img src="/src/meto_agil.png" alt="Image"  />

- Hitos y entregables (pauta de soyHenry)

Por qué decimos que es una "metodología híbrida"? 

A pesar de que todos los integrantes cumplieron su rol y sus objetivos propuestos cada semana (metodología ágil), podemos decir que también estuvimos 
cumpliendo con los objetivos propuestos por la pauta de corrección del proyecto entregada por soyHenry. Más específicamente con los "hitos y entregables" de 
cada semana, teniendo en cuenta también, los puntos importantes (o guías).

https://docs.google.com/document/d/13yU2EQ6eCFdESCwuP8pINDENgTCQCFEzSmVKqX98OL8/edit#heading=h.srjioslsjk9j

#### 3. Diseño detallado

Propuesta de trabajo: 
- Reporte en Streamlit para mejorar el proceso de ventas basado en un análisis guiado a través de un Dashboard con KPI’s y métricas, con recomendaciones para toma de decisiones.
- Aplicación en Tkinter con el objetivo de predecir los productos con mejor score basado en un modelo de  machine learning.

#### 4. Roles y responsabilidades

##### ANGEL ZAVALETA - Data Analyst
##### JOSÉ ACEVEDO - Data Engineer
##### LEONARDO CUETO - Data Engineer
##### NICOLÁS LIRA - Data Analyst

#### 5. Cronograma general

<img src="/src/Trello2.png" alt="Image" height="650" width="900" />

https://trello.com/b/zj0GHlc3/proyectofinal

## Estructura del proyecto

El proyecto tiene 2 carpetas principales: 
1) Datasets - contiene todos los archivos csv con los que se realizó el trabajo.
2) airflow
3) Olist App & ML model
4) Power BI - contiene el dashboard en formato '.pbix' y una captura de pantalla de el diagrama ER.

Los archivos importantes son:
- Olist.db - es la base de datos sobre la que trabajamos




