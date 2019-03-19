num = input("Input Number:")
s = ""
while num > 0:
    print str(num % 27) + ":" + str(num / 27)
    s = chr((num % 27) + ord('a') - 1) + s
    num /= 27

print s