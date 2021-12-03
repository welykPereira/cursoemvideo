x = 0
n = int(input('Digite um numero'))
for c in range(1, n + 1):
    if n % c == 0:
        x = x + 1

print('O numero {} foi divisivel {} vezes'.format(n, x))
if x == 2:
    print('Esse numero e primo')
else:
    print('Esse numero nao e primo!')
