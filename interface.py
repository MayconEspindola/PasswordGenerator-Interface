import tkinter as tk
from tkinter import ttk
from functools import partial
from functions import gerador_senhas, number_passwords, password_size

#Mostra uma linha
def linha():
    print("=" * 37)

#Mostra um cabeçalho
def cabecalho(mensagem = "<vazio>"):
    linha()
    print(f"{mensagem:^37}")
    linha()


class PasswordGeneratorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gerador de Senhas")

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="Quantidade:").grid(row=0, column=0, padx=10, pady=5)
        self.quant_entry = ttk.Entry(self.root)
        self.quant_entry.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(self.root, text="Tamanho:").grid(row=1, column=0, padx=10, pady=5)
        self.tam_entry = ttk.Entry(self.root)
        self.tam_entry.grid(row=1, column=1, padx=10, pady=5)

        self.create_options_frame()



    
    
        gerar_button = ttk.Button(self.root, text="Gerar Senhas", command=self.generate_passwords)
        gerar_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.resultado_text = tk.Text(self.root, height=10, width=50)
        self.resultado_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    def create_options_frame(self):
        opcoes_frame = ttk.Frame(self.root)
        opcoes_frame.grid(row=2, column=0, columnspan=2, pady=5)

        self.incluir_maiusculas_var = tk.BooleanVar(value=True)
        tk.Checkbutton(opcoes_frame, text="Incluir letras maiúsculas", variable=self.incluir_maiusculas_var).grid(row=0, column=0, padx=5)

        self.incluir_minusculas_var = tk.BooleanVar(value=True)
        tk.Checkbutton(opcoes_frame, text="Incluir letras minúsculas", variable=self.incluir_minusculas_var).grid(row=0, column=1, padx=5)

        self.incluir_numeros_var = tk.BooleanVar(value=True)
        tk.Checkbutton(opcoes_frame, text="Incluir números", variable=self.incluir_numeros_var).grid(row=0, column=2, padx=5)

        self.incluir_especiais_var = tk.BooleanVar(value=True)
        tk.Checkbutton(opcoes_frame, text="Incluir caracteres especiais", variable=self.incluir_especiais_var).grid(row=0, column=3, padx=5)

    def generate_passwords(self):
        quant = number_passwords(self.quant_entry.get())
        tam = password_size(self.tam_entry.get())

        senha_list = gerador_senhas(
            quant,
            tam,
            self.incluir_minusculas_var.get(),
            self.incluir_maiusculas_var.get(),
            self.incluir_numeros_var.get(),
            self.incluir_especiais_var.get()
        )

        self.resultado_text.delete(1.0, tk.END)  # Limpa o texto existente
        for senha in senha_list:
            self.resultado_text.insert(tk.END, senha + "\n")

    def run(self):
        self.root.mainloop()