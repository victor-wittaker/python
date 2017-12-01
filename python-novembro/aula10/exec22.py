import psycopg2

try:
    con = psycopg2.connect(
        "host=localhost dbname=escola \
        user=admin password=4linux"
    )
    cur = con.cursor()

    email = input("Insira um email: ")

    query = """
SELECT 
    *
FROM
    alunos
WHERE
    email='%s'
""" % email
    cur.execute(query)
    
    aluno = cur.fetchone()

    if aluno:
        nome = input('Insira seu novo nome: ')
        query = "\
        UPDATE \
            alunos \
        SET \
            nome='%s' \
        WHERE \
            id=%s" % (nome, aluno(0))  

        cur.execute(query)
        con.commit()
        print('Alterado com sucesso')
    else:
        print('Registro nao encontrado')
except Exception as e:
    con.rollback()
    print(e)