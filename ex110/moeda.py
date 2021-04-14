def metade(n=0, formato=False):                     # formato para identificar se é verdadeiro ou falso
    """
    -> Identifica a função para retornar a metade do valor e a opção para formatar a moeda
    :param n: Número informado
    :param formato: Opcional para Verdadeiro ou Falso
    :return: Retorna o valor
    """
    res = n / 2
    return res if not formato else moeda(res)       # retorna res sem formatação ou se vor verdadeiro retorna com a formatação da função moeda


def dobro(n=0, formato=False):
    res = n * 2
    return res if not formato else moeda(res)


def aumentando(n=0, taxa=0, formato=False):
    res = n + (n * taxa) / 100
    return res if not formato else moeda(res)


def reduzindo(n=0, taxa=0, formato=False):
    res = n + (n * taxa) / 100
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>8.2f}'.replace('.', ',')     # replica tudo que é ponto para virgúla
                                                     # alinhado a direita com 8 casas ao todo

def resumo(n=0, taxaa=10, taxar=5):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'A metade do preço: \t{metade(n, True)}')
    print(f'O dobro do preço: \t{dobro(n, True)}')
    print(f'Aumentando {taxaa}%: \t{aumentando(n, taxaa, True)}')
    print(f'Diminuindo {taxar}%: \t{reduzindo(n, taxar, True)}')
    print('-' * 30)
