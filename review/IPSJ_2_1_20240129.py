x = float(input('最高気温を入力してください : '))

if x >= 35 :
    print('猛暑日')
elif x >= 30 :
    print('真夏日')
elif x >= 25 :
    print('夏日')
elif x <= 0 :
    print('真冬日')
