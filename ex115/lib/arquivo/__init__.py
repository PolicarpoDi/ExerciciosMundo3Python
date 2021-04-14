from ex115.lib.interface import *


def arquivoexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararquivo(nome):
    try:
        a = open(nome, 'wt+')                               # criar um novo arquivo de texto
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')               # abrir o arquivo de texto
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabecalho('PESSOAS CADSATRADAS')
        for linha in a:
            dado = linha.split(';')                 # separa os dados
            dado[1] = dado[1].replace('\n', '')     # o primeiro dado recebe o dado sem o contrabarra, pois foi substituido
            print(f'{dado[0]:30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade=0):
    try:
        a = open(arq, 'at')                 # colocar mais informação no arquivo de texto
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')          # escreve dentro do arquivo
        except:
            print('Houve um erro na hora de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()