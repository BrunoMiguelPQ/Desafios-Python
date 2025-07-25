from time import sleep
print(' *.*' * 5)
print(' *    Factorial    *')
print(' *.*' * 5)
valor = int(input('\033[36mDigite o valor: \033[m'))
c = valor
f = 1
print(f'\033[33mA calcular factorial de {valor}!\033[m')
sleep(1)
while c > 0:
    print(f'\033[32m{c}\033[m', end=' ')
    print('\033[32m x \033[m' if c > 1 else '\033[32m = \033[m', end='')
    f *= c
    c -= 1
    sleep(1)
print(f'\033[33m{f}\033[m')