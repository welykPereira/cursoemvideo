try:
    casa = float(input('Qual e o valor da casa? '))
    salario = float(input('Qual e o seu salario? '))
    anos = int(input('Em quantos anos deseja financiar? '))
    prestacao = casa / (anos * 12)
    x = salario * 30 / 100
    if prestacao > x:
        print('Sua casa de valor {} parcelada em {} anos, sua parcela ficaria: R$:{} '.format(casa, anos, prestacao))
        print('30% do seu salario e {} '.format(x))
        print('Infelizmente nao podemos comprometer mais de 30% da sua renda mensal. SITUACAO NEGADA')
    else:
        print('Sua casa de valor {} parcelada em {} anos, sua parcela ficaria: R$:{} '.format(casa, anos, prestacao))
        print('30% do seu salario e {} '.format(x))
        print('Parabens vc conseguio financiar sua casa. SITUACAO APROVADA')
except:
    print('Digitou algo errado! Execute o programa novamente')
