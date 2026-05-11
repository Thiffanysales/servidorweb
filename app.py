import streamlit as st

st.title("Servidor Web")

st.header("Disciplina: Servidores e Computação em Nuvem")

st.write("Linguagem: Python.")
st.write("Os softwares: Python, Streamlit, GitHub.")
st.write("Aluna: Thiffany Cristina da Silva Sales.")

nome = st.text_input("Digite seu nome:")

if nome:
    st.write("Olá,", nome, "! Servidor funcionando.")
