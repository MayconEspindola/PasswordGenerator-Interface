#import tkinter as tk
#from tkinter import ttk
#from tkinter import messagebox
#from functools import partial
from functions import *
from interface import *

cabecalho("GERADOR DE SENHAS")

includeCapital = input("Incluir letras maiúsculas? (S/N): ").lower() == 's'
includeLower = input("Incluir letras minúsculas? (S/N): ").lower() == 's'
includeNumber = input("Incluir números? (S/N): ").lower() == 's'
includeSpecials = input("Incluir caracteres especiais? (S/N): ").lower() == 's'

quant = numberPasswords()
tam = passwordSize()

senhas = gerador_senhas(quant, tam, includeLower, includeCapital, includeNumber, includeSpecials)

cabecalho("SAINDO...")