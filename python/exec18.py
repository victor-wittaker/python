# 18 - FACA UM PROGRAMA QUE RECEBA O NOME E EMAIL DO ALUNO. 
# CADASTRE AS INFORMACOES NOME, EMAIL e DATA DE CADASTRO EM UM ARQUIVO JSON.
from datetime import datetime
import json

nome = input('Digite o nome do aluno: ')
email = input('Digite o email do aluno: ')

with open('alunos.json', 'r') as f:
    alunos = json.loads(f.read())

alunos.append(
    {
        'nome': nome,
        'email': email,
        'data': datetime.now().strftime('%d/%m/%y')
    }
)

string = json.dumps(alunos)

with open('alunos.json', 'w') as f:
    f.write(string)