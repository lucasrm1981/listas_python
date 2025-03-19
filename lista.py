#Lista frutas
lista = []
opcao = input("Digite  s/S para manipular a LISTA ou qualquer tecla para sair\n")
while opcao.upper()=="S":# transforma tudo em maiusculo caixa alta
    acao = int(input("Digite a opção desejada com a Lista:\n"
    "\n1 Adicionar um item APPEND"
    "\n2 Apagar a Lista CLEAR"
    "\n3 Copiar a Lista COPY"
    "\n4 Contar a quantidade de Elementos na lista COUNT"
    "\n5 Unir com uma Lista EXTEND"
    "\n6 subistituir um item em uma determinada posição INSERT"
    "\n7 Verificar a posição do item na lista INDEX"
    "\n8 Elementos da lista em ordem Invesa da Lista REVERSE"
    "\n9 Elementos da Lista em ordem alearória SORT\n"))
    match acao: # Após receber a posição será direcionado no caso correspondente
        case 1:
            item = input("Digite um Item para ser adicionado:\n")
            lista.append(item)# adiciona um item a lista
        case 2:
            lista.clear() # remove todos elementos da lista
        case 3:
            copia_lista  =lista.copy()# copia a lista
            print(copia_lista)
        case 4:
            print(lista)
            contador = input("Digite o item que deseja contar?")           
            print(f" o item {contador} tem {lista.count(contador)} unidades") # conta a quantidade de ocorrências na lista
        
        case 5:
            lista_carro = ["fusca", "ferrari", "furgão"]
            lista.extend(lista_carro)# União da lista_carro com a lista

        case 6:
            item = input("Digite o Item que deseja inserir\n")
            posicao = int(input("Digite a posição do item:\n"))
            lista.insert(posicao,item) # insere o elemento na posição desejada
            print(lista)
        
        case 7:
            item = input("Digite o item que deseja saber a posição")
            print(f"O item {item} está na {lista.index(item)} posição")# Visualizar a posição de um elemento da lista
        
        case 8:
            lista.reverse() # Lista de ordem inversa
            print(f"A lista será exiida de Ordem inversa\n{lista}")

        case 9:
            lista.sort() # lista de ordem aleatória
            print(f"A lista será exibida de forma aleatória\n{lista}")

    opcao=input("Digite  s/S para manipular a LISTA ou qualquer tecla para sair\n") # Pergunta para utilizar o sistema


      

