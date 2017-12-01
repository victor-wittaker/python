from urllib.request import urlopen
import json

html = urlopen('https://api.cartolafc.globo.com/mercado/destaques')
cartola_10mais = json.load(html)
index = 1

for j in cartola_10mais:
    print(index,'mais escalado')
    print("Nome:",j['Atleta']['apelido'])
    print("Time:",j['clube'],'\n')
    index += 1
     