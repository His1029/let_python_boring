import random
a = 5
r = random.randrange(10)
print('a=' + str(a))
print('r=' + str(r))
if a == r:
    print('当たり')
elif a > r:
    print('aの方が大きい')
else:
    print('aの方が小さい')
