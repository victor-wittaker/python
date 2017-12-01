# 5) FAÇA UM PROGRAMA QUE ITERE UM DICIONARIO COM NOTAS DE ALUNO, FAÇA A MEDIA E SE ELA FOR MAIOR QUE 6 IMPRIMA APROVADO, SENAO IMPRIMA REPROVADO.

alunos  = [{
    "nome": "Gabriel",
    "idade": 27,
    "email": "ganbriel@email.com",
    "notas": [ 
        5, 6, 8, 10
    ]
},
{
    "nome": "Victor",
    "idade": 27,
    "email": "victor@email.com",
    "notas": [ 
        10, 8, 5, 9, 1   
    ]
}]

for a in alunos:
    notas = 0
    for n in a["notas"]:
        notas += n
    if notas/len(a["notas"]) > 6:
        print("Aprovado, media: " + str(notas/len(a["notas"])))
    else:
        print("Nao Aprovado, media: " + str(notas/len(a["notas"])))
            

