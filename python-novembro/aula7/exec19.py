import json

email = input("Insira o email do aluno: ")

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
