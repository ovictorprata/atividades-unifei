with open("notas.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("João Aquino: 10\n")

with open("notas.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()
    print("Conteúdo atualizado do arquivo:")
    print(conteudo)
