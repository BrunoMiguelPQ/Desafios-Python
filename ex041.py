#Categorizando Atletas
from datetime import date
atual = date.today().year
DN = int(input('Digite o dia de nascimento: '))
calculo = atual - DN
if calculo <= 9:
    print('Você está na categoria MIRIM')
elif calculo <= 14:
    print('Vocá está na categoria infantil')
elif calculo <= 19:
    print('Você está na categoria JUNIOR')
elif calculo <= 25:
    print('Você está na categoria SENIOR')
else:
    print('Você está na categoria MASTER')