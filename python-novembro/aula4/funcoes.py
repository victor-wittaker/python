a = 2
b = 3

def soma():
    global a
    a = 3
    print(a)

soma()
print(a)