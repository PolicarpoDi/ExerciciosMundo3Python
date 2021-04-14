def metade(n=0):
    return n / 2


def dobro(n=0):
    return n * 2


def aumentando(n=0):
    au = (n * 10) / 100
    return n + au


def reduzindo(n=0):
    red = (n * 13) / 100
    return n - red


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>8.2f}'.replace('.', ',')     # replica tudo que é ponto para virgúla
                                                     # alinhado a direita com 8 casas ao todo