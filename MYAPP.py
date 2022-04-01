import streamlit as st
import pandas as pd

#df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

st.title("Mi primer app")
st.write(""" # My first app 
Hello *world!*""")

click = st.button("Clic")
st.write("El valor de clic es: ",click)

if click == True:
    st.image("https://www.elsoldetlaxcala.com.mx/incoming/j3sdgs-perrito.jpg/ALTERNATES/LANDSCAPE_1140/perrito.jpg")





















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
