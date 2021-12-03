soma = 0
cont = 0
for c in range(1, 501, 2):  # pulando em 2 ja temos os numeros impar
    if c % 3 == 0:  # aqui verifica se ele e multiplo de 3
        soma = soma + c
        cont = cont + 1
print('A soma de todos os {} valores solicitados e {}'.format(cont, soma))
