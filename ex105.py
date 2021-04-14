def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos
    :param n: Uma ou mais notas dos alunos (aceita varias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: Dicionário com várias unformações sobre a situação da turma
    """
    r = dict()
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n) / len(n)
    if sit:
        if r['Média'] >= 7:
            r['Situação'] = 'Boa'
        elif r['Média'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'
    return r


# Programa principal
resp = notas(5.5, 2.5, 9, 8.5)
print(resp)
help(notas)