import moeda


#Programa principal

num = float(input('Digite o valor: R$ '))
print(f'a metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando 10% de R${num} é R${moeda.aumentando(num)}')
print(f'Diminuindo 13% de R${num} é R${moeda.reduzindo(num)}')