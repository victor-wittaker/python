import json

aluno = {
    "nome": "gabriel",
    "email": "gabriel@gabriel.com"
}

string = json.dumps(aluno)
print(type(string))

## CRIANDO ARQUIVO JSON
with open('alunos.json', 'w')  as f:
    f.write(string)

## LENDO ARQUIVO JSON
with open('alunos.json', 'r') as f:
    dicionario = json.loads(f.read())

dicionario['idade'] = 27
print(dicionario)

with open('alunos.json', 'w')  as f:
    f.write(json.dumps(dicionario))

# aluno_string = '{"nome": "gabriel", "email": "gabriel@gabriel"}'
# print(type(json.loads(aluno_string)))
