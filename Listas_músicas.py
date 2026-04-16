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
        editar_musica = int(input("Número da música pra editar: ")) # Salvando número da música
        musica_alterada = "" # Criando uma caixinha pra armazenar o nome da música
        for musica in lista_musicas: # Percorrendo a lista de música

            # Salvando o nome da música caso o número dela seja o número que o usuário salvou
            if editar_musica == x: musica_alterada = musica
        print(f"Música à ser alterada: {musica_alterada}")
        nova_musica = str(input("Insira o novo nome da música ", musica_alterada, ": "))
        lista_musicas.pop(musica_alterada - 1) # Removo música antiga
        lista_musicas.append(nova_musica) # Adiciono música nova
    elif opcao == 5:
        print("Saindo...")
    else:
        print("Opcão inválida.🤡")
