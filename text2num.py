def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]

s = input("Input string:")
r = input("Block size:")

numList = [ord(c) for c in s]
print numList
blockList = list(divide_chunks(numList, r))
print blockList

for block in blockList:
    print block
    num = 0
    p = r - 1
    for n in block:
        num += n * (128 ** p)
        p -= 1
    print num
