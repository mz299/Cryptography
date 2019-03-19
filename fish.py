def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        print "{} {}".format(b, b // a)
        g, y, x = egcd(b % a, a)
        print y
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

a = input("Input a:")
p = input("Input p:")

print modinv(a, p)
