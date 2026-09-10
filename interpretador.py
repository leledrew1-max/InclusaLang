import streamlit as st

class Interpretador:

    def __init__(self):
        self.recursos = []

    def executar(self, tokens):

        i = 0

        while i < len(tokens):

            token = tokens[i]

            if token[0] == "SOLICITAR":

                recurso = tokens[i + 2][1]

                self.recursos.append(recurso)

                st.success(f"Recurso solicitado: {recurso}")

            elif token[0] == "CONSULTAR":

                recurso = tokens[i + 2][1]

                if recurso in self.recursos:
                    st.info(f"{recurso} foi solicitado.")
                else:
                    st.error(f"{recurso} não foi solicitado.")

            elif token[0] == "INSCREVER":

                curso = tokens[i + 2][1]

                st.success(f"Inscrição realizada em: {curso}")

            i += 1