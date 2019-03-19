def findGenarator(p):
    n = p - 1
    for i in xrange(2,n):
        if n % i != 0:
            continue
        if SquareAndMultiply(i, n / i, p) == 1:
            continue
        return i
    return 0

def computeGCD(x, y):

   while(y):
       x, y = y, x % y

   return x

def check_co_prime(num, M):
    return computeGCD(num, M) == 1

def get_smallest_co_prime(M):
    for i in range(2, M): # for every number *i* starting from 2 up to M
        if check_co_prime(i, M): # check if *i* is coprime with M
            return i # if it is, return i as the result

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

class ElGamal(object):
    def __init__(self, p, g):
        self.p = p
        self.g = g

    def genPub(self, priv):
        return SquareAndMultiply(self.g, priv, self.p)

    def enc(self, msg, k, pub):
        mask = SquareAndMultiply(pub, k, self.p)
        cipher = (msg * mask) % self.p
        hint = SquareAndMultiply(self.g, k, self.p)
        return cipher, hint, mask

    def dec(self, cipher, hint, priv):
        q = self.p - 1 - priv
        opener = SquareAndMultiply(hint, q, self.p)
        msg = (cipher * opener) % self.p
        return msg, opener

    def genDigitalSignatureKey(self, r):
        return SquareAndMultiply(self.g, r, self.p), get_smallest_co_prime(self.p - 1)

    def sign(self, msg, r, R):
        X = SquareAndMultiply(self.g, R, self.p)
        Y = ((msg - r * X) * modinv(R, self.p - 1)) % (self.p - 1)
        return X, Y

    def verify(self, msg, X, Y, K):
        A = (SquareAndMultiply(K, X, self.p) * SquareAndMultiply(X, Y, self.p)) % self.p
        print "A:", A
        if A == SquareAndMultiply(self.g, msg, self.p):
            return True
        return False

if __name__ == "__main__":
    p = 104801
    g = findGenarator(p)
    print "g:", g
    el = ElGamal(p, g)
    a = 29
    b = 23
    k = 57
    m = 17
    pubB = el.genPub(b)
    print "pubB:", pubB
    cipher, hint, mask = el.enc(m, k, pubB)
    print "cipher, hint, mask:", cipher, hint, mask
    msg, opener = el.dec(cipher, hint, b)
    print "msg, opener:", msg, opener

    r = 13
    K, R = el.genDigitalSignatureKey(r)
    print "K, R:", K, R
    X, Y = el.sign(msg, r, R)
    print "X, Y:", X, Y
    print el.verify(msg, X, Y, K)