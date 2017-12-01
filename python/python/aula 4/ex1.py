# FACA UM PROGRAMA QUE LEIA UM ARQUIVO TEXTO CONTENDO UMA LISTA DE ENDERECOS IP E GERE UM OUTRO ARQUIVO CONTENDO UM RELATORIO DOS ENDERECOS VALIDOS E INVALIDOS.

lista_ok = []
ip_novo = []
ip = {"ip": []}
with open("ip_exec2", "r") as f:
    for i in f.readlines():
        i = i.strip("\n")
        pos = i.split(".")
        
        print(pos)
        if int(i[:pos]) <= 255:
            print(i[:pos])
            print("i"+i)
            ip["validos"] = i
            print(ip)
        else:
            print("TESTE: " + i[:pos])
            
