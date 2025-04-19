import csv
with open("produtos.csv", "w", newline='', encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)
    writer.writerow(["ID", "Produto", "Preço"])
    writer.writerow([1, "Produto A", 10.53])
    writer.writerow([2, "Produto B", 20.79])
    writer.writerow([3, "Produto C", 15.32])