palavra = "SENAC"

print(type(palavra))

print(palavra[3])

# Exercicio de lista, for e string
palavra = "Rinoceronte"
lista = []

print("Exercicio de Lista")

print(len(palavra))

for indice in range(len(palavra)):
    lista.append(palavra[indice])

print(lista)