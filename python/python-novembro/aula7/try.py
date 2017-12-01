try:
    var = True

    if var:
        raise Exception("ERRO ENCONTRADO")
    print('TRY CONCLUIDO')
except Exception as e:
    print(e)
finally:
    print("SEMPRE RODA")
print("FIM")