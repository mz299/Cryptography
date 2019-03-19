num = input("Input Number:")
s = ""
while num > 0:
    print str(num % 128) + ":" + str(num / 128)
    s = chr(num % 128) + s
    num /= 128

print s