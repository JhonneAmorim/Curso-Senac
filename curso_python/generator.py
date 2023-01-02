# Introdução às Generator functions em Python
# generator = (n for i in range(1000000))
# Yield from

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1

        if n >= maximum:
            return


gen = generator(maximum=1000000)
for n in gen:
    # print(n)
    ...


def gen1():
    print('Começou GEN1')
    yield 1
    yield 2
    yield 3
    print('Acabou GEN1')


def gen3():
    print('Começou GEN3')
    yield 10
    yield 20
    yield 30
    print('Acabou GEN3')


def gen2(gen=None):
    print('Começou GEN2')
    if gen is not None:
        yield from gen
    yield 4
    yield 5
    yield 6
    print('Acabou GEN2')


g1 = gen2(gen1())
g2 = gen2(gen3())
g3 = gen2()

for numero in g1:
    print(numero)
print()
for numero in g2:
    print(numero)
print()
for numero in g3:
    print(numero)
print()
