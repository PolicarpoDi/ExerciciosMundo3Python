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


def aumentando(n=0, formato=False):
    res = (n * 10) / 100
    return res if not formato else moeda(res)


def reduzindo(n=0, formato=False):
    res = (n * 13) / 100
    return res if not formato else moeda(res)


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>8.2f}'.replace('.', ',')     # replica tudo que é ponto para virgúla
                                                     # alinhado a direita com 8 casas ao todo