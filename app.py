import streamlit as st
from scanner import scanner
from parser import Parser
from interpretador import Interpretador

st.title("InclusaLang")

st.write("Linguagem para Inclusão e Acessibilidade")

codigo = st.text_area(
    "Digite seu programa:",
    """INICIO

SOLICITAR(RAMPA);
CONSULTAR(RAMPA);

FIM"""
)

if st.button("Executar"):

    try:

        tokens = scanner(codigo)

        st.subheader("Tokens Encontrados")

        for token in tokens:
            st.write(token)

        parser = Parser(tokens)
        parser.programa()

        st.success("Programa sintaticamente válido!")

        st.subheader("Execução")

        interpretador = Interpretador()
        interpretador.executar(tokens)

    except Exception as erro:
        st.error(f"Erro: {erro}")