import math
print('Radar móvel analisando...')
radar = float(input('Velocidade: '))
if radar > 80:
    multa = (radar - 80) * 7
    print('Ultrapassou a velocidade minima...Multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança')