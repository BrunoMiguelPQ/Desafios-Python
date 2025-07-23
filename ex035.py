print('-='*15)
print('Analisador de triangulos')
print('-='*15)
n1 = float(input('Reta 1: '))
n2 = float(input('Reta 2: '))
n3 = float(input('Reta 3: '))
if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Podem formar um triangulo')
else:
    print('Não podem formar um triangulo')