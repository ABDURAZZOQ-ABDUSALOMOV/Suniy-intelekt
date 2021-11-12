# 1. A + B

'''a, b = map(int, input('>> ').split())
print(a+b)'''

# 2. Katta kichik

'''a, b = map(int, input('>> ').split())

if a > b:
    print('>')
elif a == b:
    print('=')
else:
    print('<')'''

# 8. Minimum va maksimum yig'indi

'''a, b, c, d, e = map(int, input().split())

lits = [a,b,c,d,e]
yigindi = 0

for i in lits:
    yigindi += i


print(yigindi - max(a, b, c, d, e), yigindi - min(a, b, c, d, e))

'''


# 21 - Partalar
'''import math

a, b, c = map(int, input('>>').split())

print(math.ceil((a+b+c)/2))'''
