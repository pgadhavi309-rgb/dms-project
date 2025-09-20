def gen():
    for i in range(1, 11):

        yield 2
        yield 4
        yield 6
        yield 8
        yield 10

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))