def computeGCD(x, y):

   while(y):
       x, y = y, x % y

   return x

def check_co_prime(num, M):
    return computeGCD(num, M) == 1

def get_smallest_co_prime(M):
    for i in xrange(2, M): # for every number *i* starting from 2 up to M
        if check_co_prime(i, M): # check if *i* is coprime with M
            return i # if it is, return i as the result

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    while a < 0:
        a = a + m
        pass
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def findD(e, psiN):
    for i in xrange(1, psiN):
        if (e * i) % psiN == 1:
            return i
    assert Exception("Not found")

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

class RSA(object):
    """docstring for RSA"""
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p * q
        self.psiN = (p - 1) * (q - 1)
        self.e = get_smallest_co_prime(self.psiN)
        self.d = modinv(self.e, self.psiN)

    def enc(self, msg):
        return SquareAndMultiply(msg, self.e, self.n)

    def dec(self, cipher):
        return SquareAndMultiply(cipher, self.d, self.n)

    def show(self):
        print "p:", self.p, "q:", self.q, "n:", self.n, "psiN:", self.psiN, "e:", self.e, "d:", self.d

    def genSignKey(self, p, q):
        m = p * q
        psiM = (p - 1) * (q - 1)
        e = get_smallest_co_prime(psiM)
        d = modinv(e, psiM)
        return m, e, d, psiM

    def sign(self, a, m, n, d, h):
        x = SquareAndMultiply(a, d, m)
        y = SquareAndMultiply(x, h, n)
        return y, x

    def verity(self, y, m, n, g, e):
        z = SquareAndMultiply(y, g, n)
        u = SquareAndMultiply(z, e, m)
        return u, z

if __name__ == '__main__':
    rsa = RSA(7, 19)
    rsa.show()
    message = 6
    c = rsa.enc(message)
    print c
    msg = rsa.dec(c)
    print msg

    p, q, r, s = 104801, 104803, 104827, 104831
    a = 12345
    m, e, d, psiM = rsa.genSignKey(p, q)
    print "m, e, d, psiM:", m, e, d, psiM
    n, h, g, psiN = rsa.genSignKey(r, s)
    print "n, h, g, psiN:", n, h, g, psiN
    y, x = rsa.sign(a, m, n, d, h)
    print "y, x:", y, x
    u, z = rsa.verity(y, m, n, g, e)
    print "u, z:", u, z

