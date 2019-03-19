def findGenarator(p):
    n = p - 1
    for i in xrange(2,n):
        if n % i != 0:
            continue
        if SquareAndMultiply(i, n / i, p) == 1:
            continue
        return i
    return 0


def SquareAndMultiply(u, m, p):
    mm = 1
    e = u
    a = 1
    aa = 0
    b = m % 2
    if b == 1:
        a = e
        aa = 1
    done = False
    while not done:
        m = (m - b) / 2
        b = m % 2
        e = (e * e) % p
        mm = mm * 2
        if b == 1:
            a = (a * e) % p
            aa += mm
        if m <= 1:
            done = True
    return a

class DiffieHellman(object):
    """docstring for DiffieHellman"""
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def genK(self, priv):
        return SquareAndMultiply(self.g, priv, self.p)

if __name__ == '__main__':
    p = 227
    g = findGenarator(p)
    print "g,", g
    a = 51
    b = 92
    df = DiffieHellman(p, g)
    ka = df.genK(a)
    kb = df.genK(b)
    print "ka, kb,", ka, kb
    pubA = SquareAndMultiply(kb, a, p)
    pubB = SquareAndMultiply(ka, b, p)
    print "pubA, pubB,", pubA, pubB
