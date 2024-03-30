def judgementofchance(num:int):
    if num % 2 == 0:
        return  '偶数'
    else:
        return  '奇数'
        

while True:
    print('偶数奇数判定を行います')
    print('数値を入力して下さい(未入力でenterキーを押すと終了できます)')
    
    num = input()
    
    if(num == ''):
        break

    print(str(num) + ' は ' + judgementofchance(int(num)))

print('数値以外が入力されました。終了します。')