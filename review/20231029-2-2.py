def judgeofnum(num:int):
    if num % 2 == 0:
        return '偶数'
    else:
        return '奇数'


while True:
    print('数値を入力してください')
    num = input('数値:')

    if num == '':
        break

    print('入力した数値は:' + judgeofnum(int(num)) + 'です')

print('数値が入力されておりません')



