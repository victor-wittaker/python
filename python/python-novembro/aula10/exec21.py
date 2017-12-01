import psycopg2

try:
    con = psycopg2.connect(
        "host=localhost dbname=escola \
        user=admin password=4linux"
    )
    cur = con.cursor()

    email = input("Insira um email: ")

    query = """
DELETE FROM
    alunos
WHERE
    email='%s'
""" % email

    cur.execute(query)
    
    con.commit()
    print('Removido com sucesso')
except Exception as e:
    con.rollback()
    print(e)