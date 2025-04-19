import pandas as pd

dados = {
    "Nome": ["Carlos", "Pedro", "Ana", "Fernanda"],
    "Idade": [25, 35, 28, 45],
    "Salário": [2500, 3500, 2800, 4200]
}
df = pd.DataFrame(dados)

print("Empregados com idade > 30:")
print(df[df["Idade"] > 30])

print("\nEmpregados com salário > 3000:")
print(df[df["Salário"] > 3000])