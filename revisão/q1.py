# estrutura:  listas 
# fala que a ordem importa 
notas = []
for i in range(1, 9):
    # repete o pedido de nota e guarda cada nota na lista
    nota = int(input(f'digite uma nota {i}:'))
    notas.append(nota)
    # adiciona a nota na lista
    print(notas)
    # mostra a lista atualizada a cada interação do for
    print(f"Maior nota: {max(notas)}")
    #maior nota da lista
    print(f"Menor nota: {min(notas)}")
    #menor nota da lista
