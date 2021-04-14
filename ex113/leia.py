def leiaint(msg):
    while True:
        try:
            i = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mO usuário preferiu não informar o número.\033[m')
            return 0
        else:
            return i


def leiafloat(msg):
   while True:
       try:
           r = float(input(msg))
       except (TypeError, ValueError):
           print('\033[0;31ERRO!Digite um número real valido!\033[m')
           continue
       except (KeyboardInterrupt):
           print('\033[31mO usuário preferiu não informar o valor!\033[m')
           return 0
       else:
           return r


