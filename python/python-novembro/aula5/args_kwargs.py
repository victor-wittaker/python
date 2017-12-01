def soma(*args, **kwargs):
    print(args)
    print(kwargs)
    # print(sum(args))

def cadastro(**kwargs):
    pass

soma(1,2,3,5,3, nome="gabriel")

cadastro(nome="Gabriel", email="gabriel@gabriel.com")