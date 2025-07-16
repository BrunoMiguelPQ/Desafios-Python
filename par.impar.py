
print('\033[35m *.*\033[m' * 8)
print(' \033[35m*\033[m        \033[34mPar ou Ímpar\033[m         \033[35m*\033[m')
print('\033[35m *.*\033[m' * 8)
while True:
    número = int(input('Escolha um número: '))

    if número % 2 == 0:
        print('\033[33mPar\033[m')
    else:
        print('\033[33mImpar\033[m')

    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('\033[31mComando Inválido!\033[m')
    if resp == 'N':
        break
print('\033[31mPrograma encerrado. Volte sempre! ')
