while True:
    print('数値を入力してください')
    num = int(input())
    if num % 2 == 0 :
        print('偶数')
    elif num % 2 == 1 :
        print('奇数')
    break
print('終了')