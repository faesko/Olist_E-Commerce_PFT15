import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

iconslg=Image.open('images\icon.png')

#Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="SLG-Analitycs", page_icon=iconslg, layout="wide")

def load_lottieurl(url):
     r = requests.get(url)
     if r.status_code !=200:
          return None
     return r.json()

# Use Local CSS
def local_css(file_name):
     with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- Load Assets ----
lottie_code = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_QUXmIu.json")
lottie_commerce = load_lottieurl('https://assets8.lottiefiles.com/packages/lf20_hu9cd9.json')
objetivo = load_lottieurl('https://assets8.lottiefiles.com/private_files/lf30_ltuqrtmn.json')
img_KPI3_form = Image.open('images\KP13.png')
img_ciclo_form = Image.open('images\ciclodevida.png')
integrantes = Image.open('images\integrantes.png')
banner = Image.open('images\slgbi.jpg')
tk = Image.open('images\Tkinter.png')
ciclodata = Image.open('images\data.png')


# ---- Banner ---
st.image(banner, width=1200)

# ---- Header Section ----
st.subheader("Servicio de Consultoría en Business Inteligence: ")
st.title("Olist-Ecommerce")
st.write("Con el proposito de brindar soluciones de consultoria efectivas, SLG-BI presenta el siguiente reporte de Analisis de Datos Funcional para proyectar oportunidades de mejora en los procesos de venta para la empresa Olist")

# --- What I Do ----

with st.container():
     st.write("---")
     st.header("Entendimiento de la Situación")
     st.write('##')
     image_column, text_column = st.columns((1,3))

     with image_column:
          st_lottie(lottie_commerce, height=300, key= "coding")

     with text_column:
          st.subheader('E-commerce en la actualidad.')
          st.write(
               '''
               El e-commerce ha crecido rápidamente en los últimos años y es una pieza fundamental en  la economía mundial. 
El e-commerce permite a las empresas alcanzar una base de clientes más amplia, cómoda y con un menor costo operativo en su desarrollo.

Una de las principales ventajas del e-commerce es la capacidad de recopilar datos sobre el comportamiento, las preferencias y los hábitos de compra de los clientes y mejorar sus ofertas con el tiempo.

Olist nos contrata como consultores externos para encontrar soluciones innovadoras que permitan a sus usuarios vender sus productos a un mayor número de clientes. 
               '''
          )

with st.container():
     st.write("---")
     st.header("Objetivos")
     st.write('##')
     text_column, image_column = st.columns((3,1))
     
     with image_column:
          st_lottie(objetivo, height=300, key= "cod")

     with text_column:
          st.subheader('Especificos')
          st.write(
               '''
               Objetivo: Reducir el tiempo de ingreso (aceptación) de los clientes potenciales a Olist, para aumentar sus ganancias.
               
               Objetivo: Identificar las tendencias de ventas por categorías de productos a través del tiempo, ayudando a Olist a descubrir oportunidades comerciales por temporada.
               
               Objetivo: Establecer un ranking de productos con mejor score basado en el indice de popularidad, logrando posicionar los productos que generen mayor rentabilidad.
               '''
          )
          st.markdown('')

with st.container():
     st.write("---")
     st.header("Ciclo de Vida del Dato")
     st.write('##')
     image_column, text_column = st.columns((1,1))
     
     with image_column:
          st.image(ciclodata)

     with text_column:
          st.write(
               '''
               -La información procesada hace uso principal del lenguaje de programación Python, 

-iniciando con la "Extracción" de datos por medio de Técnología Pandas que continua en la "Transformación" haciendo uso de Pandas y Numpy, 

-posteriormente la carga de datos es realizada con SQLite y SQAlquemy para dar forma al Data Warehouse, este ciclo es iterativo teniendo como objetivo principal la actualizacion, que es asistida por librería Airblow permitiendo a su vez automatizar tareas indispensables en el proceso de ETL. 

-La finalidad es lograr dos productos, el primero, un Reporte Web diseñado con Streamlit, que permite integrar la totalidad del proyecto y destaca la interfaz interactiva del Dashboard realizado en Power Bi El segundo producto la aplicación de escritorio Olist Report Viewer construido con la librería Tkinter de Python misma que a su vez añade una función de Machine Learning lograda con la tecnología scikit Learn.
               '''
          )

with st.container():
     st.write("---")
     left_column, right_column = st.columns(2)
     with left_column:
          st.header('DashBoard')
          st.write('##')
          st.write(
               '''
               Como parte de la visualización de datos SLG-BI presenta un DASHBOARD que integra tres dimensiones analisis:
               
               1: Relación de postulantes aceptados e ingreso mensual declarado.

               2: Tendencia de ventas por categoría y trimestre.

               3: Ranking de productos con mejores ventas  y coeficiente de popularidad.

               '''
          )
          
     st.write('')

with right_column:
     st_lottie(lottie_code, height=300, key= "code")

iframe = """
<iframe title="Report Section" width="1280" height="720" src="https://app.powerbi.com/view?r=eyJrIjoiMDBmYzkyNTgtNDM1My00YTI4LWIyZTUtMDcwMmRlOTcyMmVlIiwidCI6ImQ4Mzk0YjJhLTA5Y2YtNDkzNi1hZTM0LThiMGU5MjkwMzRkNSJ9" frameborder="0" allowFullScreen="true"></iframe>
"""
with st.container():
     st.write("---")
     st.markdown(iframe, unsafe_allow_html=True)

# --- Projects ----

#cogido de PowerBI


with st.container():
     st.write("---")
     st.header("Aplicación Olist Report Viewer")
     st.write('##')
     image_column, text_column = st.columns((1,1))
     
     with image_column:
          st.image(tk)

     with text_column:
          st.subheader('Tkinter + ScikitLearn')
          st.write(
               '''
               Recomendamos el uso de tkinter por parte de Olist para consumir la base de datos de manera
               fácil y eficiente, ademas de contar con una herramienta de Machine Learning
               que predice la popularidad de productos que generen mayor ganancia para Olist.
               '''
          )
          

with st.container():
     st.write("---")
     st.header("Acerca de SLG-BI, Analitycs")
     st.write('##')
     image_column, text_column = st.columns((1,2))
     
     with image_column:
          st.image(integrantes)

     with text_column:
          st.subheader('Team SGL-Bi Analitycs')
          st.write(
               '''
               Angel Zavaleta - Data Analyst

               José Acevedo - Data Engineer

               Leonardo Cueto - Data Engineer

               Nicolas Lira - Data Analyst
               '''
          )

with st.container():
     st.write('---')
     st.header('Contactanos!')
     st.write('##')

     #Documentación: https://formsubmit.co/
     contact_form = '''
          <form action="https://formsubmit.co/zavaletacode@gmail.com" method="POST">
          <input type="hidden" name ="_captcha" value= "false">
          <input type="text" placeholder="Your name" required>
          <input type="email" placeholder="Your email" required>
          <textarea name= "message" placeholder="Your message here" required ></textarea>
          <button type="submit">Send</button>
     </form>
     '''

     left_column, right_column = st.columns(2)
     with left_column: 
          st.markdown(contact_form, unsafe_allow_html=True)
     with right_column:
          st.empty()
#https://github.com/Leonardo1278/PFT15_OLIST_ECOMERCE