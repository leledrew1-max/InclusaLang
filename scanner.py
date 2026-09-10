import re

TOKENS = [
    ("INICIO", r"INICIO"),
    ("FIM", r"FIM"),
    ("SOLICITAR", r"SOLICITAR"),
    ("INSCREVER", r"INSCREVER"),
    ("CONSULTAR", r"CONSULTAR"),
    ("LPAREN", r"\("),
    ("RPAREN", r"\)"),
    ("PONTOVIRG", r";"),
    ("ID", r"[A-Z_]+"),
]

def scanner(texto):
    tokens = []

    while texto:
        texto = texto.lstrip()

        if not texto:
            break

        encontrou = False

        for nome, padrao in TOKENS:
            match = re.match(padrao, texto)

            if match:
                valor = match.group(0)
                tokens.append((nome, valor))
                texto = texto[len(valor):]
                encontrou = True
                break

        if not encontrou:
            raise Exception(f"Token inválido: {texto}")

    return tokens