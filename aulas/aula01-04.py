# programa para trabalhar nome e idade
nome  = input('Digite o nome da pessoa ')
idade = int(input('Digite a idade '))

if (idade > 50):
    print(f"{nome} tem {idade} anos e é experiente.")
else:
    print(f"{nome} tem {idade} anos, está em treinamento")

