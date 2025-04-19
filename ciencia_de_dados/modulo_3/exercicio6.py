import pandas as pd

dados = {
    "Aluno": ["João", "Maria", "José", "Ana"],
    "Nota 1": [7.5, 8.2, 6.9, 9.1],
    "Nota 2": [8.0, 7.5, 6.5, 9.5]
}
df = pd.DataFrame(dados)

print(df["Aluno"])

print("\nPrimeira linha:")
print(df.iloc[0])

aluno_jose = df[df["Aluno"] == "José"]
media_jose = aluno_jose[["Nota 1", "Nota 2"]].mean(axis=1).values[0]
print(f"\nMédia das notas de José: {media_jose}")