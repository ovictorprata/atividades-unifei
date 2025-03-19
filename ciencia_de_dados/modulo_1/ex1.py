valor_conta = float(input("Digite o valor da conta: R$ "))
percentual_desconto = float(input("Digite o percentual de desconto: "))
desconto = (percentual_desconto / 100) * valor_conta
novo_valor = valor_conta - desconto
print(f"O valor com desconto é: R$ {novo_valor:.2f}")
