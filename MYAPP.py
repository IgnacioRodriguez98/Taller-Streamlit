import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv')

st.title("Mi primer app")
st.write(""" # My first app 
Hello *world!*
""")
if st.button("No hacer clic"):
    st.write("Te dije que no lo hicieras")
else:
    st.write("Gracias por no hacer clic")

st.button("Entrar a los recursos")
st.write(df)
