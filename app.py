import streamlit as st
import pandas as pd

from scanner import scanner
from parser import Parser
from interpretador import Interpretador

# MENU LATERAL

st.sidebar.title("🎓 InclusaLang")

pagina = st.sidebar.radio(
    "Navegação",
    [
        "🏠 Demonstração",
        "📋 BNF",
        "📋 EBNF",
        "🎯 ODS",
        "👩‍💻 Sobre"
    ]
)

# BNF

if pagina == "📋 BNF":

    st.title("📋 Gramática BNF")

    st.code("""
<programa> ::= INICIO <lista_comandos> FIM

<lista_comandos> ::= <comando>
                   | <comando> <lista_comandos>

<comando> ::= SOLICITAR(<id>);
            | CONSULTAR(<id>);
            | INSCREVER(<id>);

<id> ::= ID
""")

    st.stop()

# EBNF

if pagina == "📋 EBNF":

    st.title("📋 Gramática EBNF")

    st.code("""
programa = "INICIO", lista_comandos, "FIM";

lista_comandos = { comando };

comando =
    "SOLICITAR", "(", id, ")", ";"
  | "CONSULTAR", "(", id, ")", ";"
  | "INSCREVER", "(", id, ")", ";";

id = ID;
""")

    st.stop()

# ODS

if pagina == "🎯 ODS":

    st.title("🎯 Objetivos de Desenvolvimento Sustentável")

    st.markdown("""
### ODS 10 – Redução das Desigualdades

- Meta 10.2: promover a inclusão social.
- Meta 10.3: garantir igualdade de oportunidades.

### ODS 4 – Educação de Qualidade

- Meta 4.5: eliminar disparidades de acesso à educação.
- Meta 4.a: promover ambientes educacionais inclusivos.
""")

    st.stop()

# SOBRE

if pagina == "👩‍💻 Sobre":

    st.title("👩‍💻 Sobre o Projeto")

    st.markdown("""
### InclusaLang

Projeto desenvolvido para a disciplina de **Linguagens Formais e Compiladores**.

**Universidade:** UNIG

**Curso:** Ciência da Computação

**Autora:** Alessandra Brito Araújo

### Tecnologias Utilizadas

- Python
- Streamlit
- GitHub
- Scanner Léxico
- Parser Descendente Recursivo
- Interpretador
""")

    st.stop()

# DEMONSTRAÇÃO

st.title("🎓 InclusaLang")

st.markdown("""
### Linguagem Formal para Inclusão e Acessibilidade

Projeto desenvolvido para a disciplina de **Linguagens Formais e Compiladores**.

ODS 10 • Redução das Desigualdades
""")

st.divider()

st.subheader("📝 Programa de Entrada")

codigo = st.text_area(
    "Digite seu programa:",
    """INICIO

SOLICITAR(RAMPA);
CONSULTAR(RAMPA);

FIM""",
    height=250
)

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

        df = pd.DataFrame(dados)

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True
        )

        parser = Parser(tokens)
        parser.programa()

        st.success(
            "✅ Análise Sintática Concluída: Programa Válido"
        )

        st.divider()

        st.subheader("⚙️ Resultado da Execução")

        interpretador = Interpretador()
        interpretador.executar(tokens)

    except Exception as erro:
        st.error(f"❌ Erro: {erro}")

st.divider()

st.caption(
    "InclusaLang • Linguagens Formais e Compiladores • UNIG"
)