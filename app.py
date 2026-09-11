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
        "📊 Aplicação Prática",
        "📋 BNF",
        "📋 EBNF",
        "🎯 ODS",
        "👩‍💻 Sobre"
    ]
)

# APLICAÇÃO PRÁTICA

if pagina == "📊 Aplicação Prática":

    st.title("📊 Aplicação Prática da InclusaLang")

    st.markdown("""
### 📌 Simulação de Uso Real

A InclusaLang pode ser utilizada para registrar e acompanhar
solicitações de acessibilidade em instituições de ensino,
projetos sociais e ambientes inclusivos.

Os dados apresentados possuem finalidade acadêmica e ilustram
uma possível aplicação prática da linguagem.
""")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Solicitações",
        "38"
    )

    col2.metric(
        "Recursos",
        "4"
    )

    col3.metric(
        "Atendimentos",
        "31"
    )

    st.divider()

    nome = st.text_input(
        "Nome do Solicitante"
    )

    recurso = st.selectbox(
        "Recurso de Acessibilidade",
        [
            "RAMPA",
            "LEITOR_TELA",
            "MATERIAL_ADAPTADO",
            "CURSO_PROGRAMACAO"
        ]
    )

    if st.button("📨 Registrar Solicitação"):

        if nome.strip() == "":

            st.warning(
                "Informe o nome do solicitante."
            )

        else:

            st.success(
                f"Solicitação de {recurso} registrada para {nome}."
            )

    st.divider()

    st.subheader("📈 Recursos Mais Solicitados")

    dados = pd.DataFrame(
        {
            "Solicitações": [15, 10, 8, 5]
        },
        index=[
            "RAMPA",
            "LEITOR_TELA",
            "MATERIAL_ADAPTADO",
            "CURSO_PROGRAMACAO"
        ]
    )

    st.bar_chart(dados)

    st.caption(
        "Dados simulados para demonstração acadêmica."
    )

    st.info(
        "Esta funcionalidade apresenta uma simulação de utilização da InclusaLang em um cenário real de gerenciamento de solicitações de acessibilidade."
    )

    st.stop()

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

st.subheader("🧪 Casos de Teste")

teste = st.selectbox(
    "Escolha um cenário para demonstração:",
    [
        "✅ Programa Válido",
        "❌ Erro Sintático",
        "🔍 Consulta Não Encontrada"
    ]
)

# CASOS DE TESTE

if teste == "✅ Programa Válido":

    codigo_padrao = """INICIO

SOLICITAR(RAMPA);
CONSULTAR(RAMPA);

FIM"""

elif teste == "❌ Erro Sintático":

    codigo_padrao = """INICIO

SOLICITAR(RAMPA)

FIM"""

elif teste == "🔍 Consulta Não Encontrada":

    codigo_padrao = """INICIO

CONSULTAR(LEITOR_TELA);

FIM"""

st.divider()

st.subheader("📝 Programa de Entrada")

codigo = st.text_area(
    "Digite seu programa:",
    value=codigo_padrao,
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
        st.error(
            f"❌ Erro: {erro}"
        )

st.divider()

st.caption(
    "InclusaLang • Linguagens Formais e Compiladores • UNIG"
)