#forループ
total = 0

for num in range(5): #5回繰り返す、6回目で抜ける
    total = total + num

    print('num = ' + str(num))
    print('total = ' + str(total))
print(total)
