from interface import *
from random import choice
from time import sleep

senha = [] # lista vazia

def checkInt(inter):
    while True:
        try:
            inter = int(input(inter))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite apenas números inteiros!\033[m")
            continue
        else:
            return inter
        break

def numberPasswords(): #quantas senhas serão pedidas
    quant = checkInt("Quantidade: ")
    return quant

def passwordSize(): #Tamanho da senha
    tam = checkInt("Tamanho das senhas: ")
    return tam

#Gerador de senhas
def gerador_senhas(quant, tam, includeLower, includeCapital, includeNumber, includeSpecials):
    cabecalho("GERANDO SENHAS...")
    sleep(1)

    strings = ""

    if includeLower:
        strings += "abcdefghijklmnopqrstuvwxyz"
    if includeCapital:
        strings += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if includeNumber:
        strings += "0123456789"
    if includeSpecials:
        strings += "!@#$%^&*()_-+=<>?"
    if not strings:
        print("ERRO! Nenhuma opção de caracteres selecionada.")
        return

    for senha_gerada in range(0, int(quant)):
        senha = [choice(strings) for _ in range(int(tam))]
        senha_str = "".join(senha)
        print(senha_str)

    sleep(1)
    cabecalho("SENHAS GERADAS COM SUCESSO!")