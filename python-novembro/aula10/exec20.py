import psycopg2

try:
    con = psycopg2.connect(
        "host=localhost dbname=escola \
        user=admin password=4linux"
    )
    cur = con.cursor()

    nome = input("Insira um nome: ")
    email = input("Insira um email: ")

    query = """
INSERT INTO
    alunos
    (nome,email)
VALUES
    ('%s', '%s')
""" % (nome, email)

    cur.execute(query)
    
    con.commit()
    print('Adicionado com sucesso')
except Exception as e:
    con.rollback()
    print(e)