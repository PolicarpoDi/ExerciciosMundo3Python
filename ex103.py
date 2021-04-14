def ficha(jog='<Desconhecido>', gols=0):    # vai trazer essas informações caso não seja preenchido
    print(f'O jogador {jog} fez {gols} gols no campeonato.')


# Programa principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))       # deixa como string para validação, pois apresenta erro caso não informar nada
if g.isnumeric():                        # se o g for numérico
    g = int(g)                           # g recebe inteiro de g
else:
    g = 0                                # senão recebe 0
if n.strip() == '':                      # se o campo nome estiver vazio
    ficha(gols=g)                        # só mostra a quantidade de gols informada
else:
    ficha(n, g)                          # se estiver informado o nome monstra o gol e o nome