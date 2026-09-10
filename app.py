import streamlit as st
import pandas as pd

from scanner import scanner
from parser import Parser
from interpretador import Interpretador

# SIDEBAR

st.sidebar.title("🎓 InclusaLang")

st.sidebar.info("""
Alessandra Brito Araújo

Ciência da Computação - UNIG

Trabalho Final

ODS 10 - Redução das Desigualdades
""")

# CABEÇALHO

st.title("🎓 InclusaLang")

st.markdown("""
### Linguagem Formal para Inclusão e Acessibilidade

Projeto desenvolvido para a disciplina de **Linguagens Formais e Compiladores**.

ODS 10 • Redução das Desigualdades
""")

st.divider()

# ENTRADA

st.subheader("📝 Programa de Entrada")

codigo = st.text_area(
    "Digite seu programa:",
    """INICIO

SOLICITAR(RAMPA);
CONSULTAR(RAMPA);

FIM""",
    height=250
)

# BOTÃO

if st.button("🚀 Executar Programa"):

    try:

        tokens = scanner(codigo)

        st.divider()

        st.subheader("📋 Tokens Encontrados")

        dados = []

        for token in tokens:
            dados.append({
                "Tipo": token[0],
                "Valor": token[1]
            })

        st.dataframe(
            pd.DataFrame(dados),
            use_container_width=True
        )

        parser = Parser(tokens)
        parser.programa()

        st.success("✅ Programa sintaticamente válido!")

        st.divider()

        st.subheader("⚙️ Resultado da Execução")

        interpretador = Interpretador()
        interpretador.executar(tokens)

    except Exception as erro:
        st.error(f"❌ Erro: {erro}")

# RODAPÉ

st.divider()

st.caption(
    "InclusaLang • Linguagens Formais e Compiladores • UNIG"
)