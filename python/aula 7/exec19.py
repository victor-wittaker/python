#19 - FACA UM PROGRAMA QUE RECEBA O EMAIL DO ALUNO E 
# RETORNE O NOME E A DATA DE CADASTRO NO FORMATO DD-MM-YYYY
import json

email = input("Digite o email do aluno: ")

with open('alunos.json', 'r') as f:
    alunos = json.loads(f.read())

for a in alunos:
    if a['email'] == email:
        print('Nome: ' + a['nome'])
        print('Email: ' + a['email'])
        print('Data: ' + a['data'])
        break
else: 
    print('Nao encontrado')