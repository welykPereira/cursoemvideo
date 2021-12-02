
n1 = int(input('Digite o 1 numero!'))
n2 = int(input('Digite o 2 numero!'))

if n1 > n2:
    print('O numero {} e maior que o {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} e maior que o {}'.format(n2, n1))
else:
    print('O numero {} e igual ao {} '.format(n1, n2))