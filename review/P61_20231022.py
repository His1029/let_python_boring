# 数当てゲーム
import random
secret_nunber = random.randint(1,20)
print('1から20までの数を当ててください')

# 6回聞く
for i in range(1,7):
    print('数を入力してください')
    guess = int(input('数:'))
    
    if guess < secret_nunber:
        print('あなたの推定値は小さいです。')
    elif guess > secret_nunber:
        print('あなたの推定値は大きいです。')
    else:
        break #　当たり！

if guess == secret_nunber :
        print('当たり！' + str(i) + '回で当たりました！')
else :
        print('残念。正解は' + str(secret_nunber) + 'でした。')






