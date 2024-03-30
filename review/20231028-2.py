while True:
    try:
        print('数字を入力してください')
        num = int(input())
        if num % 2 == 0:
            print('偶数')
        elif num % 2 == 1:
            print('奇数')
        break
    except:
        print('数字以外を入力されました')
print('正しく入力されました')
    
