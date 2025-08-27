'''
    programa para definir se um 
    número é par ou ímpar
'''
def verificarParImpar(numero):
    if (numero % 2 == 0):
        return 'O número é par'
    else:
        return 'O número é ímpar'
    
valor = int(input('Digite um número '))

print(verificarParImpar(valor))