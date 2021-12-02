from datetime import datetime
now = datetime.now()
#print(now.year)
anoAgora = now.year
anoNasc = int(input('Digite seu ano de nacimento!'))
idade = anoAgora - anoNasc
if idade == 18:
    print('Voce tem {} anos.Essa e a hora de se alistar! boa sorte.'.format(idade))
elif idade < 18:
    print('Voce tem {} anos. Voce ainda vai se alistar daqui {} anos'.format(idade, 18 - idade))
else:
    print('Vc tem {} anos .Ja passou {} anos do prazo para se alistar'.format(idade, idade - 18))
