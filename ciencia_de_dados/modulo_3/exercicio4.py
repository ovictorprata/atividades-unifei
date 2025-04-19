import csv
with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.DictReader(arquivo)
    for linha in reader:
        print(f"Produto: {linha['Produto']}, Preço: R${linha['Preço']}")