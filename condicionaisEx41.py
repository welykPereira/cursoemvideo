from datetime import datetime
now = datetime.now()
ano = now.year
anoNasc = int(input('Digite seu ano de nacimento!'))
idade = ano - anoNasc
if idade < 9:
    print('Voce tem {} anos!'.format(idade))
    print('Sua categoria e MIRIM')
elif idade >= 9 and idade < 14:
    print('Voce tem {} anos!'.format(idade))
    print('Sua categoria e INFANTIL')
elif idade >= 14 and idade < 19:
    print('Voce tem {} anos!'.format(idade))
    print('Sua categoria e Junior')
elif idade >= 19 and idade == 20:
    print('Voce tem {} anos!'.format(idade))
    print('Sua categoria e SENIOR')
else:
    print('Voce tem {} anos!'.format(idade))
    print('Sua categoria e Master')
