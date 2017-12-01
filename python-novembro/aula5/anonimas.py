var = lambda x: x * 2

print(var(2))

var = [
    lambda x: x + 2,
    lambda x: x * 2,
    lambda x: x - 2
]

for a in var:
    print(a(10))

print(var[1](10))