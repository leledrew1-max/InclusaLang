from scanner import scanner
from parser import Parser
from interpretador import Interpretador

with open("programa.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

tokens = scanner(conteudo)

print("TOKENS ENCONTRADOS:\n")

for token in tokens:
    print(token)

parser = Parser(tokens)
parser.programa()

print("\nEXECUÇÃO:\n")

interpretador = Interpretador()
interpretador.executar(tokens)