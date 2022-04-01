import streamlit as st
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')
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
num1 = st.slider("Escoge el primer número",0,300,15)
num2 = st.slider("Escoge el segundo número",0,300,15)

st.write("La suma de esos números es:", num1+num2)



















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
