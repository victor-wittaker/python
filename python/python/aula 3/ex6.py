# 6) FAÇA UM PROGRAMA QUE RECEBA UM NÚMERO. SE O NÚMERO FOR MENOR QUE 0 ou MAIOR QUE 10 PEÇA NOVAMENTE, SENÃO, ENCERRE O PROGRAMA.

num = int(input("Digite o numero: "))
while num < 0 or num > 10:
    num = int(input("Digite o numero novamente: "))
else:
        exit(0)
     
