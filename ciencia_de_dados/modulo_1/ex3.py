altura = float(input("Digite a altura da pessoa (em metros): "))
sexo = input("Digite o sexo da pessoa (h para homem, m para mulher): ")

if sexo.lower() == "h":
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == "m":
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = None

if peso_ideal:
    print(f"O peso ideal para essa pessoa é: {peso_ideal:.2f} kg")
else:
    print("Sexo inválido. Digite 'h' para homem ou 'm' para mulher.")
