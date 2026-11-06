#100 unidades no stock
n = int(input("quantidade de operações: "))
estoque = [100]
#valor original do stock, por isso que criei a lista com 100 
i=1
while i <= 6:
    operacao = int(input())
    valor = estoque[i-1] + operacao
    #o i-1 é para pegar o valor anterior do stock, e somar com a operação
    estoque.append(valor)
    if valor < 0:
        break
    i=i+1
print(estoque)
