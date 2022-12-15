

def exibir_cardapio(cardapio):                            # Define função que exibe o cardápio

    for i, v in enumerate(cardapio):                      # Varre a lista cardapio atribuindo em i e v, o indice e valor
        print(f"[{i}] - {v[0]} - {v[1]}")                 # Imprime o cardápio, substituindos os valores entre chaves pelas respectivas variáveis


def exibir_menu(menu):                                    # Define função que exibe o menu

    for i, v in enumerate(menu):                          # Varre a lista menu atribuindo em i e v, o indice e valor
        print(f"[{i}] {v}")                               # Imprime o menu, substituindos os valores entre chaves pelas respectivas variáveis


def adicionar_item(cardapio):                            # Define função que adiciona um item ao pedido

    item = int(input("O que deseja? "))                  # Recebe a entrada do usuário após o cast para int
    return cardapio[item]                                # Retorna um item específio do cardápio


def fechar_pedido(pedido):                               # Define função para fechar o pedido do cliente

    total = 0                                            # Define a variável total com o valor 0
    print("Este é o seu pedido:")                        # Imprime a mensagem especificada
    for x in pedido:                                     # Percorre a lista de pedido pondo em X cada um desses itens
        print(x)                                         # Imprime o conteudo de x na tela
        valor = x[1]                                     # Recebe a string na posição 1 da lista contida em x
        valor = int(valor[3:])                           # Faz um cast para inteiro do fatiamento da string guardada em valor
        total += valor                                   # O total é incrementando pelo valor contido em x na posição 1.
    print("")                                            # Pula uma linha para melhorar durante a execução do programa
    print(f"O valor total do pedido é de R${total}")     # Imprime o menu para escolha do usuario, substituindo o valor entre chaves pela respectiva variável
    print("Obrigado pela preferencia e volte sempre")    # Imprime a mensagem especificada