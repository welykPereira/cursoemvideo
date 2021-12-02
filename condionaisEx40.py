
nota1 = float(input('Digite sua primeira nota!'))
nota2 = float(input('Digite sua primeira nota!'))
media = (nota1 + nota2) / 2
if media < 5:
    print('Sua media e de {} portanto vc esta REPROVADO!'.format(media))
elif media > 5 and media <= 6.9:
    print('Sua media e de {} portanto vc esta em RECUPERACAO!'.format(media))
else:
    print('Sua media e de {} portanto vc esta APROVADO'.format(media))
