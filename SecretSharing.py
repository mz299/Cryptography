
class SecretSharing(object):
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.n = n
        self.m = m
        self.table = []

    def gen(self, n, m):
        for i in xrange(1, 2 * n + m):
            k = i
            Xk = 0
            if i % 2 == 1:
                Xk = (i + 1) / 2
            if i % 2 == 0:
                Xk = -i / 2
            Yk = a*Xk*Xk*Xk + b*Xk*Xk + c*Xk + d
            self.table.append([k, Xk, Yk])
            pass

    def show(self):
        for item in self.table:
            print item



if __name__ == "__main__":
    a, b, c, d = 1, 7, 26, 5
    n, m = 5, 8
    ss = SecretSharing(a, b, c, d)
    ss.gen(n, m)
    ss.show()