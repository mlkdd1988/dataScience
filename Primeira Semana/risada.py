risada = input()
risadaVogais = ""
vogais = "aeiou"

for c in risada:
    if(c in vogais):
        risadaVogais+=c

#print(risadaVogais[::-1]) inverte

engracada = True
tamRisada = len(risadaVogais)
for i in range(tamRisada):
    if risadaVogais[i] != risadaVogais[tamRisada-i-1]:
        engracada = False

if engracada:
    print("S")
else:
    print("N")