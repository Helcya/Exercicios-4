lista = ('Monitor', 849.99, 'Estabilizador', 319.99, 'Impressora', 279.99)
i = 0
print("*******Listagem de Preços*******")
for c in range(0, len(lista)+1):
    if(i != len(lista)):
        print(lista[i], "........", "R$", lista[i+1])
        i += 2