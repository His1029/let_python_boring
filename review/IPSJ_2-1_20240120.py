print('点数を入力してください :',end = '')
x = int(input())

if x >= 90:
    print('S:Excellent')
elif x >= 80:
    print('A:Good!')
elif x >= 70:
    print('B:Average')
else:
    print('poor')