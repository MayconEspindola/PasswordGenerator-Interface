def separator():
    print("=" * 37)

#Mostra um cabeçalho
def cabecalho(mensagem = "<vazio>"):
    separator()
    print(f"{mensagem:^37}")
    separator()