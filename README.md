# InclusaLang

## Descrição

InclusaLang é uma linguagem formal desenvolvida para o registro de solicitações de recursos de acessibilidade e inclusão social.

O projeto foi desenvolvido para a disciplina de Linguagens Formais e Compiladores e está alinhado ao ODS 10 (Redução das Desigualdades) e ao ODS 4 (Educação de Qualidade).

---

## Demonstração Online

A aplicação foi publicada utilizando Streamlit Community Cloud.

🔗 https://inclusalang-unig.streamlit.app

---

## Funcionalidades

- Scanner Léxico
- Parser Descendente Recursivo
- Interpretador
- Interface Web com Streamlit
- Casos de Teste Interativos
- Aplicação Prática Simulada
- Demonstração Online

---

## Comandos

- SOLICITAR(RECURSO);
- CONSULTAR(RECURSO);
- INSCREVER(CURSO);

---

## Casos de Teste

A aplicação disponibiliza cenários prontos para demonstração:

- ✅ Programa Válido
- ❌ Erro Sintático
- 🔍 Consulta Não Encontrada

---

## Exemplo

```text
INICIO

SOLICITAR(RAMPA);
CONSULTAR(RAMPA);

FIM
```

---

## Estrutura do Projeto

```text
InclusaLang/
│
├── app.py
├── main.py
├── scanner.py
├── parser.py
├── interpretador.py
├── programa.txt
├── README.md
└── RELATORIO_INCLUSALANG.pdf
```

---

## Tecnologias Utilizadas

- Python
- Streamlit
- GitHub
- Expressões Regulares
- Análise Léxica
- Análise Sintática
- Parser Descendente Recursivo

---

## Objetivos de Desenvolvimento Sustentável

### ODS 10 – Redução das Desigualdades

- Meta 10.2: promover a inclusão social.
- Meta 10.3: garantir igualdade de oportunidades.

### ODS 4 – Educação de Qualidade

- Meta 4.5: eliminar disparidades no acesso à educação.
- Meta 4.a: promover ambientes educacionais inclusivos.

---

## Funcionalidades da Aplicação Web

A interface web permite:

- Executar programas escritos em InclusaLang.
- Visualizar os tokens gerados pelo Scanner Léxico.
- Validar a sintaxe por meio do Parser Descendente Recursivo.
- Executar comandos através do Interpretador.
- Consultar a gramática BNF.
- Consultar a gramática EBNF.
- Visualizar os ODS relacionados ao projeto.
- Executar casos de teste pré-configurados.

---

## Aplicação Prática Simulada

A aplicação disponibiliza uma seção de simulação de uso real, demonstrando como a InclusaLang poderia ser utilizada futuramente para registrar e acompanhar solicitações de acessibilidade.

Nesta área, o usuário pode:

- Informar um nome de solicitante;
- Selecionar um recurso de acessibilidade;
- Registrar solicitações simuladas;
- Visualizar indicadores e gráficos demonstrativos;
- Compreender uma possível aplicação prática da linguagem em ambientes educacionais e sociais.

**Observação:** os dados apresentados possuem caráter acadêmico e ilustrativo.

---

## Autora

Alessandra Brito Araújo

---

## Disciplina

Linguagens Formais e Compiladores

Curso de Ciência da Computação – UNIG

---

## Repositório Acadêmico

Projeto desenvolvido como atividade prática da disciplina de Linguagens Formais e Compiladores, contemplando:

- Especificação de uma linguagem formal;
- Gramática BNF e EBNF;
- Scanner Léxico;
- Parser Descendente Recursivo;
- Interpretador;
- Autômato Finito Determinístico;
- Interface Web;
- Aplicação Prática Simulada;
- Demonstração Online.
