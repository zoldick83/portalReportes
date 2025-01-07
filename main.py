import streamlit as st #libreria para realizar pagina
import pandas as pd #libreria es para ciencia de datos
import plotly.express as px #libreria de graficos
import datetime #la coloque para el calendario


st.markdown(
        """
            #### Esto estara en todas las Paginas
            - esto es un item
        """
    )
def paginaPrincipal():
    st.title("Pagina Principal")
    st.write("Bienvenido a tu portal de reportes")

    age = st.slider("How old are you?", 0, 130, 25)
    st.write("I'm ", age, "years old")
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")
    
   


def paginaReporte():
    st.title("Reportes")
    st.write("Carga un archivo csv para ver tus estadisticas")
    archivo = st.file_uploader("Selecciona tu archivo", type='csv')
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.write("Los datos de tu archivo")
        for i in range(len(df)):
            st.write(df.iloc[i]['ALE'])
        st.write(df)

def paginaGraficos():
    st.title("Graficos")
    d = st.date_input("When's your birthday", datetime.date(2019, 7, 6))
    st.write("Your birthday is:", d)
    archivo = st.file_uploader("Selecciona tu archivo", type='csv', key="2" )
    if archivo is not None:
        df = pd.read_csv(archivo)
        st.line_chart(df)
        st.bar_chart(df)

def paginaPrueba():
    st.title("llama a funcion")
    salida = datos()
    st.write(salida)

def datos():
    return {'nombre':'Alexis'}

st.sidebar.title("Navegacion")
pagina= st.sidebar.selectbox("Selecciona un Pagina",["pagina1","pagina2","pagina3","pagina4"])

if pagina == "pagina1":
    paginaPrincipal()
elif pagina == "pagina2":
    paginaReporte()
elif pagina == "pagina3":
    paginaGraficos()
elif pagina == "pagina4":
    paginaPrueba()
    
    
