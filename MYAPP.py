import streamlit as st
st.title("Mi primer app")
st.write(""" # My first app 
Hello *world!*
""")
if st.button("No hacer clic"):
    st.write("Te dije que no lo hicieras")
else:
    st.write("Gracias por no hacer clic")

st.button("Entrar a los recursos")
