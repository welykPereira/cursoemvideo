from random import seed
from random import randint

cadastros = [] #lista
cadastro = {} # Dicionario
while True:
    print('-' * 10, 'MENU', '-' * 10)
    print('1 - NOVA INSCRICAO')
    print('2 - Visualizar INSCRICAO')
    print('0 - Encerrar')
    print('-' * 25)
    op = int(input('Digite a opcao desejada \n'))
    while op == 1:
        cadastro.clear()
        seed(100)
        numero = randint(1, 400)
        cadastro['voucher'] = numero
        cadastro['nome'] = str(input('Digite seu nome: '))
        cadastro['email'] = str(input('Digite seu e-mail'))
        cadastro['telefone'] = int(input('Digite seu telefone '))
        cadastro['curso'] = str(input('Digite seu curso'))
        cadastros.append(cadastro.copy())
        print('Cadastro Realizado com sucesso!')
        break
    if op == 2:
        if not cadastro.values():
            print('Nenhum cadastro')
        else:
            for e in cadastros:
                for i, j in e.items():
                    print('{} : {} '.format(i, j))
    elif op == 0:
        print('Encerrando programa!............')
        break
    elif op != 1 and op != 2 and op != 0:
        print('Digite uma opcao valida!')
