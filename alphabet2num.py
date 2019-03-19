def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

s = input("Input string:")
s = s.lower()
r = input("Block size:")

numList = [ord(c) - ord('a') for c in s]
print numList
blockList = list(divide_chunks(numList, r))
print blockList

for block in blockList:
    print block
    num = 0
    p = r - 1
    for n in block:
        num += n * (26 ** p)
        p -= 1
    print num
