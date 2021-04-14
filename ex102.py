def fatorial(n, show=False):
    """
    -> Calcula o fatorial de um número
    :param n: número que será fatorado
    :param show: (opcional) para mostrar ou não o calculo
    :return: o valor do fatorial de um numero n
    """

    f = 1
    for c in range(nun, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
nun = int(input('Digite o numero para ser fatorado: '))
print(fatorial(fatorial(nun), show=False))