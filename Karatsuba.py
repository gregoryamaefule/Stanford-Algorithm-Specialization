def main():
    x = input('X: ')
    y = input('Y: ')
    x = int(x)
    y = int(y)
    print(Karatsuba(x,y))

def Karatsuba(x,y):
    if len(str(x)) == len(str(y)):
        n = len(str(x))
    elif len(str(x)) > len(str(y)):
        n = len(str(x))
        y = '0'*(len(str(x))-len(str(y))) + str(y)
        y = int(y)
    elif len(str(y)) > len(str(x)):
        n = len(str(y))
        x = '0'*(len(str(y)) - len(str(x))) + str(x)
        x = int(x)


    if n == 1:
        return x*y
    else:
        mid = n/2
        a, b = [str(x)[0:mid], str(x)[mid:]]
        c, d = [str(y)[0:mid], str(y)[mid:]]

        a = int(a)
        b = int(b)
        c = int(c)
        d = int(d)

        p = a + b
        q = c + d

        ac = Karatsuba(a, c)
        bd = Karatsuba(c, d)
        pq = Karatsuba(p, q)

        adbc = pq - ac - bd

        p1 = int(str(ac) + '0'*n)
        p2 = int(str(adbc) + '0'*mid)
        p3 = bd

        return p1 + p2 + p3


main()
