def makelist(n):
    l = []

    for i in range(n):
        l.append(i)

    return l

def recursive_makelist_1(n, i=0, a=None):
    # "a" is a common name for the "accumulator"... the variable that
    # accumulates the result as the algorithm runs

    if a is None:
        a = []

    if i == n:
        return a

    # list(a) makes a copy of the list
    # This would be a more "functional" way of thinking of things
    a_copy = list(a)
    a_copy.append(i)

    return recursive_makelist_1(n, i + 1, a_copy)

def recursive_makelist_2(n, i=0, a=None):
    if a is None:
        a = []

    if i == n:
        return a

    # But in this case, just using the same list works, too
    a.append(i)

    return recursive_makelist_2(n, i + 1, a)

def recursive_makelist_2_inner(n):
    # Same, but with an inner function that doesn't mod the outer signature

    def inner(n, i, a):
        if a is None:
            a = []

        if i == n:
            return a

        # But in this case, just using the same list works, too
        a.append(i)

        return inner(n, i + 1, a)

    return inner(n, 0, [])

def loop1(n):
    while n > 0:
        print(n)
        n -= 1

def loop2(n):
    if n == 0:
        return

    print(n)
    loop2(n-1)

loop2(5)

print(makelist(10))
print(recursive_makelist_1(10))
print(recursive_makelist_2(10))
print(recursive_makelist_2_inner(10))
