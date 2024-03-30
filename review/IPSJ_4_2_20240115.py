import random

a = 5
r = random.randrange(1,11)

print('a =',a,'r=',r)

if a == r:
    print('当たり')
elif a > r :
    print('aの方が大きい')
elif a < r :
    print('aの方が小さい')

