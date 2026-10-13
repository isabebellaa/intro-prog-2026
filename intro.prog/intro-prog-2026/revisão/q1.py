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
    print (f"Média: {sum(notas)/len(notas):.0f}")
    #:.0f formata a média para 0 casas decimais
    #sum soma todos os elementos da lista e divide pelo tamanho da lista
    #len retorna o tamanho da lista


pos = int(input("nota a ser alterada (1-8): "))
if 1 <= pos <= 8:
    nova_nota = int(input(f"nova nota: "))
    notas [pos-1] = nova_nota
    print(notas)
    # [pos-1] pois a lista começa do 0 e o usuário começa do 1
else: 
    print("posição inválida")

