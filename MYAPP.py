import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
########################### Uso de titulo y write#############################################
st.title("Mi primer app")
st.write(""" # My first app 
Hello *world!*""")
##################################Uso de Boton ################################################
click = st.button("Clic")
st.write("El valor de clic es: ",click)

if click == True:
    st.image("https://www.elsoldetlaxcala.com.mx/incoming/j3sdgs-perrito.jpg/ALTERNATES/LANDSCAPE_1140/perrito.jpg")

##################################Uso de Slider ##########################
with st.sidebar:
    st.write(""" # Calculadora
    ## Suma""")
    num1 = st.slider("Escoge el primer número",0.0,300.0,15.0)
    num2 = st.slider("Escoge el segundo número",0.0,300.0,15.0)
    st.write("La suma de esos números es:", num1+num2)
    st.write("## Multiplicación")
    num3 = st.number_input("Escribe el primer número")
    num4 = st.number_input("Escribe el segundo número")

    st.write("La multiplicación de esos números es:", num3*num4)


















#st.latex("\int_1^6 sin(x)dx")
#if st.button("No hacer clic"):
#    st.write("Te dije que no lo hicieras")
#else:
#    st.write("Gracias por no hacer clic")

#st.button("Entrar a los recursos")
#st.write(df)
#st.map(df)
#st.markdown("""# Este es un titulo
#""")
