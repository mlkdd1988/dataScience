import requests
import json


def requisicao(titulo):
    try:
        base_url = 'https://api.themoviedb.org/3/search/movie?api_key=92fe8b681828c0b6c0658b436751b412&query='
        url = base_url +titulo
        req = requests.get(url)
        filmes = json.loads(req.text)
        return filmes

    except:
        print('Erro na conexao')
        return  None


def printar_detalhes(filmes):
    print
    for filme in filmes['results']:
        print('Título:', filme['title'])


sair = False
while not sair:
    op = input('Escreva o nome de um filme ou SAIR para fechar:')
    if op == 'SAIR':
        sair = True
    else:
        filmes = requisicao(op)
        if filmes == None:
            print('Filme não encontrado')
        else:
            printar_detalhes(filmes)