#Peça 5 notas e mostre a média. Diga se o aluno foi aprovado (média ≥ 6).

print('\033[35m *.*\033[m' * 8)
print(' \033[35m*\033[m       \033[34mMédia e Situação\033[m      \033[35m*\033[m')
print('\033[35m *.*\033[m' * 8)
total = 0
contador = 0
while True:
    for c in range(1, 6):
        nota = float(input(f'Digite sua {c} nota: '))
        total += nota
        contador += 1
    media = total / contador
    print(f'\033[33mA média das 5 notas foi: {media:.2f}\033[m')

    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()
        if resp in 'S, N':
            break
        print('\033[31mERRO!Responda só com S ou N!\033[m')
    if resp == 'N':
        break

print('\033[31mEncerrando programa!\033[m')