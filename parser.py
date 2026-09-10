class Parser:

    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def token_atual(self):
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return None

    def consumir(self, tipo):
        token = self.token_atual()

        if token and token[0] == tipo:
            self.pos += 1
        else:
            esperado = tipo
            encontrado = token[0] if token else "EOF"
            raise Exception(
                f"Esperado {esperado}, encontrado {encontrado}"
            )

    def programa(self):
        self.consumir("INICIO")

        while self.token_atual() and self.token_atual()[0] != "FIM":
            self.comando()

        self.consumir("FIM")

        print("\nPrograma sintaticamente válido!")

    def comando(self):

        token = self.token_atual()

        if token[0] == "SOLICITAR":
            self.consumir("SOLICITAR")

        elif token[0] == "INSCREVER":
            self.consumir("INSCREVER")

        elif token[0] == "CONSULTAR":
            self.consumir("CONSULTAR")

        else:
            raise Exception(
                f"Comando inválido: {token}"
            )

        self.consumir("LPAREN")
        self.consumir("ID")
        self.consumir("RPAREN")
        self.consumir("PONTOVIRG")
