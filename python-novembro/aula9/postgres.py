import psycopg2

try:
    # CONEXAO COM O BANCO
    con = psycopg2.connect(
        "host=localhost dbname=escola \
        user=admin password=4linux"
    )

    # INICIA UMA SESSAO
    cur = con.cursor()

    # INSERIR REGISTRO
    cur.execute(
        "INSERT INTO alunos(nome, email) \
        VALUES('Joao assunção', 'joao@j.com')"
    )

    # DELETAR REGISTRO
    # cur.execute(
    #     "DELETE FROM alunos WHERE id = 1"
    # )

    # ATUALIZAR REGISTRO
    # cur.execute(
    #     "UPDATE alunos SET email='joao@jao.com'"
    # )

    # SELECIONAR TODOS OS REGISTROS
    cur.execute(
        "SELECT * FROM alunos"
    )

    alunos = cur.fetchall()
    for a in alunos:
        print(a)

    # SELECIONA UM REGISTRO
    cur.execute(
        "SELECT * FROM alunos \
        WHERE id=1"
    )

    print(cur.fetchone())

    # con.commit()
except Exception as e:
    con.rollback()
    print(e)
finally:
    con.close()