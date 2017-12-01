import MySQLdb
try:
    con = MySQLdb.connect(
        host="127.0.0.1",
        user="root",
        passwd="123456",
        db="escola"
    )

    cur = con.cursor()

    cur.execute(
        "INSERT INTO clientes(nome, endereco) \
        VALUES('Joao assunção', 'rua um')"
    )

    con.commit()
except Exception as e:
    con.rollback()
    print(e)
finally:
    con.close()