import json
from datetime import datetime

nome = input("Insira o nome do aluno: ")
email = input("Insira o email do aluno: ")

with open('alunos.json', 'r') as f:
    alunos = json.loads(f.read())

alunos.append(
    {
        "nome": nome,
        "email": email,
        "data": datetime.now().strftime('%d/%m/%Y')
    }
)

string = json.dumps(alunos)

with open('alunos.json', 'w') as f:
    f.write(string)