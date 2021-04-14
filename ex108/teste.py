from ex108 import moeda


#Programa principal

num = float(input('Digite o valor: R$ '))
print(f'a metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10% de {moeda.moeda(num)} é {moeda.moeda(moeda.aumentando(num))}')
print(f'Diminuindo 13% de {moeda.moeda(num)} é {moeda.moeda(moeda.reduzindo(num))}')