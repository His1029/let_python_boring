def judgementofchance(num):
    ans =''
    if num % 2 == 0:
        answer = '偶数'
    else:
        answer = '奇数'
    
    return answer
        

while True:
    print('偶数奇数判定を行います')
    print('数値を入力して下さい(未入力でenterキーを押すと終了できます)')
    
    num = input()
    
    if(num == ''):
        break

    print(str(num) + ' は ' + judgementofchance(int(num)))

print('終了します。またのご利用をお待ちしております。')
