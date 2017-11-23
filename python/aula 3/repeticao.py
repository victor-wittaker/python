## WHILE ===========================================

x = 1

while x < 10:
    print(x)
    x += 1
##    x = x + 1
else:
    print("OVER")

## FOR =============================================

## lista
fruta = ["Laranja", "Melancia", "Uva"]

for f in  fruta:
    print(f)
    print(fruta.index(f))

## tupla

aluno  = {
    "nome": "Gabriel",
    "idade": 27,
    "email": "ganbriel@email.com",
    }

for a, b in aluno.items():
    print(a, b)
     


## dicionario

alunos  = [{
    "nome": "Gabriel",
    "idade": 27,
    "email": "ganbriel@email.com",
    "notas": [ 
        5, 6, 8, 1
    ]
},
{
    "nome": "Victor",
    "idade": 27,
    "email": "victor@email.com",
    "notas": [ 
        3, 8, 2, 9    
    ]
}]


for a in alunos:
    notas = 0
    for n in a["notas"]:
        notas += n
    print("Alunos: %s Nota %s" % (a["nome"], notas))



