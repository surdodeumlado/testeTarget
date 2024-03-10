def fibonacci(numero):
    a, b = 0, 1
    if numero == a or numero == b:
        return True

    while b <= numero:

        a, b = b, a + b
        if b == numero:
            return True

    return False


while True:
    try:
        entrada = input('Informe um número (ou "sair" para encerrar): ')
        if entrada.lower() == 'sair':
            break

        numero = int(entrada)

        if fibonacci(numero):
            print(f'{entrada} Faz parte da sequência de Fibonacci.')
            continue

        print(f'{entrada} Não faz parte da sequência de Fibonacci.')

    except ValueError:
        print('Por favor, informe um número inteiro válido ou "sair" para encerrar.')
