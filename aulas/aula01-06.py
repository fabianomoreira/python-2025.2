# cálculo de média e exibição de resultado
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2)/2

if(media > 6.5):
    situacao = "Aprovado"
else:
    situacao = "Reprovado"

if (media > 0) and (media <= 10):
    print(f"A média foi {media}. O aluno está {situacao}.")
else:
    print(f"Inconsistência nas notas informadas.")