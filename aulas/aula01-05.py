# programa para trabalhar nome e idade
nome  = input('Digite o nome da pessoa ')
idade = int(input('Digite a idade '))
sexo = input('Digite o gênero - (Masculino ou Feminino) ')

if (sexo.upper() == "MASCULINO"):
    sexo = "M"
elif (sexo.upper() == "FEMININO"):
    sexo = "F"
else:
    sexo = "Gênero não esperado"

if (idade > 50):
    print(f"{nome} tem {idade} anos e é experiente ({sexo}).")
else:
    print(f"{nome} tem {idade} anos, está em treinamento ({sexo}).")

