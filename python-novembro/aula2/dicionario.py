var = {
    "turma": "1234",
    "curso": "Python Basic",
    "alunos": [
        {
            "nome": "Gabriel",
            "idade": 27
        },
        {
            "nome": "Joao",
            "idade": 18
        }
    ]
}

print(var['alunos'][1]['nome'], var['alunos'][1]['idade'])

var['alunos'][1]['nome'] = 'Michelle'

print(var.get('regiao'))

print(type(var))

x, y, z = ['a', 'b', 'c']

var = {"nome": "Gabriel", "email": "gabriel@gabriel"}

a, b = var.items()

print(a)
print(b)

print(var.values())