# Sistema de fastfood v3.0

# IMPORTS:

import main_library as main_lib

# ENTRADAS:

cardapio = [("Coca Cola", "R$ 8"), ("Água Mineral", "R$ 4"), ("Suco", "R$ 10"),   # Cria uma lista com os itens do cardápio e seu valor
            ("Hot dog", "R$ 15"), ("Batata frita", "R$ 12"), ("Coxinha", "R$ 7"),
            ("Hamburguer", "R$ 20"), ("Milk shake", "R$ 18")]

pedido = []                                                          # Define uma lista vazia

menu = ["Adicionar item", "Fechar pedido", "Cancelar pedido"]        # Cria uma lista com as opções do sistema


print("")                                                            # Pula uma linha para melhorar durante a execução do programa
print("Bem vindo ao Krusty Burguer")                                 # Imprime a mensagem especificada
print("")                                                            # Pula uma linha para melhorar durante a execução do programa
print("Veja nosso cardápio!")                                        # Imprime a mensagem especificada

# PROCESSAMENTO:

main_lib.exibir_cardapio(cardapio)                                  # Chama a função exibir_cardapio, passando como parametro o cardápio
item = int(input("O que deseja: "))                                 # Recebe a entrada do usuário após o cast para int
pedido.append(cardapio[item])                                       # Adiciona na lista pedido o item selecionado pelo cliente

while True:                                                         # Entra em looping até que uma considação de saída seja dada

    print("")                                                       # Pula uma linha para melhorar durante a execução do programa
    main_lib.exibir_menu(menu)                                      # Chama a função exibir_menu
    op = int(input("Escolha uma opção: "))                          # Recebe a entrada do usuário após o cast para int

    if op == 0:                                                     # Verifica se a opção foi adicionar item

        print("")                                                   # Pula uma linha para melhorar durante a execução do programa
        main_lib.exibir_cardapio(cardapio)                          # Chama a função exibir_cardapio, passando como parametro o cardápio
        pedido.append(main_lib.adicionar_item(cardapio))            # Adicionao ao pedido o item que foi escolhido no cardapio

    elif op == 1:                                                   # Verifica se a opção foi Fechar pedido

        print("")                                                   # Pula uma linha para melhorar durante a execução do programa
        main_lib.fechar_pedido(pedido)                              # Chama a função fechar_pedido, passando como parametro o pedido
        break                                                       # interrompe o loop e finaliza a execução da aplicação

    elif op == 2:                                                   # Verifica se a opção foi cancelar pedido
        print("Seu pedido foi cancelado")                           # Imprime a mensagem especificada
        pedido = []                                                 # Zera a lista do pedido

    else:                                                           # Executa este bloco caso nenhuma das opções tenha sido escolhida
        print("Opção inválida, escolha outra opção!")               # Imprime a mensagem especificada
