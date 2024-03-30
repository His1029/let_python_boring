while True:
    try:
        print('数値を入力してください:',end = '') #入力補助＆改行なし
        num = int(input())
        if num % 2 == 0 :
            print('偶数')
        elif num % 2 == 1 :
            print('奇数')
        break
    except:
        print('数値以外が入力されました')
print('正しく入力されました')