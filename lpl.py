import time

input('Pressione Enter para começar')
while True:
    nome = str(input('Digite: '))
    for letra in nome:
        print(letra, end='', flush=True)
        time.sleep(1)
    print()
    input('Digite "Sair" para sair').lower()
    if input() == 'sair':
        break

