print('\033[35m *.*\033[m' * 4)
print(' \033[35m*\033[m   \033[34mTabuada\033[m   \033[35m*\033[m')
print('\033[35m *.*\033[m' * 4)

while True:
    t = int(input('Que tabuada deseja saber?: '))
    for c in range(1, 11):
        print(f'{t:} x {c:>2} = {t*c:>2}')

    while True:
        resp = str(input('\033[33mQuer continuar? [S/N]: \033[m')).strip().upper()[0]

        if resp in 'SN':
            break
        print('\033[31mDigite apena S ou N!\033[m')

    if resp == 'N':
        break

print('\033[31mEncerrando Programa!')