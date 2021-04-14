from ex109 import moeda


#Programa principal

num = float(input('Digite o valor: R$ '))
print(f'a metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10% de {moeda.moeda(num)} é {moeda.aumentando(num, True)}')
print(f'Diminuindo 13% de {moeda.moeda(num)} é {moeda.reduzindo(num, True)}')
