import requests
import json

def getClima(nomeCidade):
    try:
        url = 'https://api.openweathermap.org/data/2.5/weather?appid=929f39e8b0fa3d5b14902837ef19e3b4&q='+nomeCidade
        req = requests.get(url)
        clima = json.loads(req.text)
        return clima
    except:
        print('Erro na conexao')
        return None

def printClima(clima):
    if clima is not None:
        print(clima['weather'][0]['description'])

#Main
nomeCidade = input('Digite o nome da cidade que deseja conhecer o clima:')
clima = getClima(nomeCidade)
printClima(clima)