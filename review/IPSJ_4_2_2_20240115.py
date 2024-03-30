import random

r = random.randrange(1,10)
a = int(input('aの数を入力してください:'))
print('a =',a,'r=',r)

while a != r :
    r = random.randrange(1,10)
    a = int(input('数を入力してください:'))
    print('a =',a,'r=',r)
print('当たり！')

    