import requests
import json

def getCotacoes():
    try:
        url = 'https://api.hgbrasil.com/finance?format=json&key=e09a74d1'
        requisicao = requests.get(url)
        cotacoes = json.loads(requisicao.text)
        return cotacoes
    except:
        print('Erro na conexao')
        return None

def printCotacoes(cotacoes):
    print('Moeda:Valor de compra')
    if cotacoes is not None:
        for cotacao in cotacoes['results']['currencies']:
            if cotacao['name'] is not None:
                print(cotacao['name'])
                print(cotacao['buy'])

#Main
print("Cotações:")
cotacoes = getCotacoes()
printCotacoes(cotacoes)

