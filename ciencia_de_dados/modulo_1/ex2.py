usuarios = []

while True:
    print("\nMENU:")
    print("1 = Incluir usuário")
    print("2 = Excluir usuário")
    print("3 = Consultar usuário")
    print("4 = Alterar usuário")
    print("5 = Listar todos os usuários")
    print("9 = Sair")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        nome = input("Digite o nome do usuário: ")
        usuarios.append(nome)
        print(f"Usuário {nome} incluído com sucesso!")
    elif opcao == 2:
        nome = input("Digite o nome do usuário a ser excluído: ")
        if nome in usuarios:
            usuarios.remove(nome)
            print(f"Usuário {nome} excluído com sucesso!")
        else:
            print("Usuário não encontrado.")
    elif opcao == 3:
        nome = input("Digite o nome do usuário a ser consultado: ")
        if nome in usuarios:
            print(f"Usuário {nome} está cadastrado.")
        else:
            print("Usuário não encontrado.")
    elif opcao == 4:
        nome = input("Digite o nome do usuário a ser alterado: ")
        if nome in usuarios:
            novo_nome = input("Digite o novo nome: ")
            usuarios[usuarios.index(nome)] = novo_nome
            print(f"Usuário {nome} alterado para {novo_nome} com sucesso!")
        else:
            print("Usuário não encontrado.")
    elif opcao == 5:
        if usuarios:
            print("Usuários cadastrados:")
            for usuario in usuarios:
                print(usuario)
        else:
            print("Não há usuários cadastrados.")
    elif opcao == 9:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
