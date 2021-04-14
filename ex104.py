def leiaint(msg):
    ok = False                                          # declara um variavel para validar se esta ok
    valor = 0                                           # valor digitado
    while True:
        i = str(input(msg))                             # input da leitura do n
        if i.isnumeric():                               # se o n for numerico
            valor = int(i)                              # valor vai receber n
            ok = True                                   # confirmação validada
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
        if ok:
            break                                       # se o ok for validade para o laço
    return valor


#Programa principal
i = leiaint('Digite um número: ')                       # função leiaint
print(f'Você acabou de digiar o número {i}.')