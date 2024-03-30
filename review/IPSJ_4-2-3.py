import random
a = int(input('1から10までの適当な数を入力してください:'))
r = random.randrange(11)
print('a =',a   , 'r=',r) 
if a == r: 
    print('当たり')
elif a > r :
    print('aの方が大きい')
elif a < r :
    print('aの方が小さい')
    