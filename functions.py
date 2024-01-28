from random import choice
from time import sleep
from tkinter import simpledialog

def check_int(inter):
    while True:
        try:
            inter = int(simpledialog.askstring("Input", inter))
        except (ValueError, TypeError):
            print("\033[0;31mERRO! Digite apenas números inteiros!\033[m")
            continue
        else:
            return inter
        break


def number_passwords(quant):
    return check_int(f"Quantidade ({quant}): ")

def password_size(tam):
    return check_int(f"Tamanho das senhas ({tam}): ")

import string

def generate_password(allowed_chars, length):
    return ''.join(choice(allowed_chars) for _ in range(length))

def generate_allowed_chars(include_lower, include_capital, include_number, include_specials):
    allowed_chars = ""
    
    if include_lower:
        allowed_chars += string.ascii_lowercase
    if include_capital:
        allowed_chars += string.ascii_uppercase
    if include_number:
        allowed_chars += string.digits
    if include_specials:
        allowed_chars += "!@#$%^&*()_-+=<>?"

    return allowed_chars

def gerador_senhas(quant, tam, include_lower, include_capital, include_number, include_specials):
    sleep(1)

    allowed_chars = generate_allowed_chars(include_lower, include_capital, include_number, include_specials)

    if not allowed_chars:
        messagebox.showerror("Erro", "Nenhuma opção de caracteres selecionada.")
        return []

    senha_list = [generate_password(allowed_chars, int(tam)) for _ in range(int(quant))]

    for senha in senha_list:
        print(senha)

    sleep(1)
    return senha_list