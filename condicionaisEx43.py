print('-' * 15)
print('-' * 5, 'IMC', '-' * 5)
print('-' * 15)
while True:
    try:
        peso = float(input('Digite seu peso!'))
        altura = float(input('Digite sua altura!'))
        break
    except:
        print('Digite algo valido')

imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC e de {}. Portanto vc esta abaixo do peso'.format(imc))
elif imc >= 18.5 and imc < 25:
    print('Seu IMC e de {}. Portanto vc esta no peso ideal'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC e de {}. Portanto vc esta com Sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC e de {}. Portanto vc esta com obesidade'.format(imc))
else:
    print('Seu IMC e de {}. Portanto vc esta com obesidade morbida'.format(imc))
