import csv
with open("produtos.csv", "r", encoding="utf-8") as arquivo:
    reader = csv.DictReader(arquivo)
    produtos = [(linha["ID"], linha["Produto"], round(float(linha["Preço"]) * 0.9, 2)) for linha in reader]

with open("produtos_desconto.csv", "w", newline='', encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["ID", "Produto", "Preço com Desconto"])
    for prod in produtos:
        writer.writerow(prod)