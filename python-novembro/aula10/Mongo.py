from pymongo import MongoClient

class Mongo:
    db = None

    def __init__(self, host, base):
        client = MongoClient(host)
        self.db = client[base]

    def inserir(self, nome, email):
        return self.db.alunos.insert(
            {
                "nome": nome,
                "email": email
            }
        )

    
    def alterar(self, **kwargs):
        return self.db.alunos.update(
            {"email": kwargs['email']},
            {
                "$set": kwargs
            }
        )
    
    def remover(self, email):
        return self.db.alunos.remove(
            {
                "email": email
            }
        )

    def buscar(self, email):
        return self.db.alunos.find(
            {
                "email": email
            }
        )