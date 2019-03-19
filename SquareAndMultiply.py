# u = input("Input u:")
# m = input("Input m:")
# p = input("Input p:")

# mm = 1
# e = u
# a = 1
# aa = 0
# b = m % 2
# if b == 1:
#     a = e
#     aa = 1
# done = False
# print "m:{:<4d} b:{:<4d} mm:{:<4d} e:{:<4d} aa:{:<4d} a:{:<4d}".format(m, b, mm, e, aa, a)
# while not done:
#     m = (m - b) / 2
#     b = m % 2
#     e = (e * e) % p
#     mm = mm * 2
#     if b == 1:
#         a = (a * e) % p
#         aa += mm
#     if m <= 1:
#         done = True
#     print "m:{:<4d} b:{:<4d} mm:{:<4d} e:{:<4d} aa:{:<4d} a:{:<4d}".format(m, b, mm, e, aa, a)

# print a

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

if __name__ == "__main__":
    print SquareAndMultiply(3, 118, 23);