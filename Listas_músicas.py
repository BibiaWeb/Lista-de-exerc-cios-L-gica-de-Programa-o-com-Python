# Crie uma variável que adiciona uma música
# Adicione essa música na listas
# Faça um FOR para exibir todas as músicas da lista
# Adicione outra música na lista
# Remova a primeira música da lista
# Exiba novamente a lista, mas com um print.

lista_musicas = ["Levo Comigo", "Anjos", "Nosso Lugar", "Aquarela"] # Lista de Músicas
nova_musica = "" # Variável para adicionar nova música
opcao = 0
while opcao != 2:
    print("O que você dejesa fazer?")
    print("🙄[1] - Adicionar música")
    print("🤨[2] - Visualizar músicas")
    print("😭[3] - Apagar música")
    print("😶[4] - Editar música")
    print("😬[5] - Sair")
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nova_musica = str(input("Nova música:"))
        lista_musicas.append(nova_musica)
        print("Música", nova_musica, "Adicionado com sucesso!🤩")
    elif opcao == 2:
        print("===============")
        x = 1
        for musica in lista_musicas:
            print(x, " - ", musica)
            x = 1
    elif opcao == 3:
        print("===============")
        x = 1
        for musica in lista_musicas:
            print(x, " - ", musica)
            x = 1
        deletar_musica = int(input("Número da música pra apagar: "))
        lista_musicas.pop(deletar_musica - 1)
    elif opcao == 5:
        print("Saindo...")
    else:
        print("Opcão inválida.🤡")
