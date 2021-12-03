soma = 0
cont = 0
for c in range(1, 7, 1):
    n = int(input('Digite um valor!'))
    if n % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('O total de pares digitados foi de {}'.format(cont))
print('A soma de todos os pares {} '.format(soma))
