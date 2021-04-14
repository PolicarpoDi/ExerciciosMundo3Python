import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.google.com.br')
except:
    print('Erro ao tentar acessar!')
else:
    print('Você conseguiu acessar!')
