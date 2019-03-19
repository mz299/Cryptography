
class ZeroKnowledge(object):
    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.N = p * q

    def genPub(self, s1, s2):
        p1, p2, i = 0, 0, 0
        while p1 == 0 and i < self.N:
            if s1 * s1 * i % self.N == 1:
                p1 = i
            i = i + 1
        i = 0
        while p2 == 0 and i < self.N:
            if s2 * s2 * i % self.N == 1:
                p2 = i
            i = i + 1
        return p1, p2

    def genABC(self, abc):
        return [abc[0] * abc[0] % self.N, abc[1] * abc[1] % self.N, abc[2] * abc[2] % self.N]

    def challenge(self, abc, matrix, s1, s2):
        M = abc[0] * s1 ** matrix[0][0] * s2 ** matrix[0][1] % self.N
        P = abc[1] * s1 ** matrix[1][0] * s2 ** matrix[1][1] % self.N
        Q = abc[2] * s1 ** matrix[2][0] * s2 ** matrix[2][1] % self.N
        return [M, P, Q]

    def verify(self, ABC, MPQ, matrix, p1, p2):
        flag = True
        if MPQ[0] * MPQ[0] * p1 ** matrix[0][0] * p2 ** matrix[0][1] % self.N != ABC[0]:
            print "M:", MPQ[0] * MPQ[0] * p1 ** matrix[0][0] * p2 ** matrix[0][1] % self.N, " != A:", ABC[0]
            flag = False
        if MPQ[1] * MPQ[1] * p1 ** matrix[1][0] * p2 ** matrix[1][1] % self.N != ABC[1]:
            print "P:", MPQ[1] * MPQ[1] * p1 ** matrix[1][0] * p2 ** matrix[1][1] % self.N, " != B:", ABC[1]
            flag = False
        if MPQ[2] * MPQ[2] * p1 ** matrix[2][0] * p2 ** matrix[2][1] % self.N != ABC[2]:
            print "Q:", MPQ[2] * MPQ[2] * p1 ** matrix[2][0] * p2 ** matrix[2][1] % self.N, " != C:", ABC[2]
            flag = False
        return flag




if __name__ == "__main__":
    zk = ZeroKnowledge(43, 47)
    s1, s2 = 12, 32
    p1, p2 = zk.genPub(s1, s2)
    print p1, p2
    abc = [42, 15, 63]
    ABC = zk.genABC(abc)
    print ABC
    matrix = [[0, 1], [1, 0], [1, 1]]
    MPQ = zk.challenge(abc, matrix, s1, s2)
    print MPQ
    print zk.verify(ABC, MPQ, matrix, p1, p2)


