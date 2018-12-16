import re
string_teste = 'o gato, o gatinho e o gatão são bonitos'

padrao = re.findall(r'gat\w*',string_teste)

if padrao:
    print(padrao)
else:
    print('Padrao nao encontrado')
