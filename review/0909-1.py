def koyama(warizan):
    try:
        return 42 / warizan
    except ZeroDivisionError:
        print('ゼロ除算が発生しました。\n不正な引数です。')

print(koyama(2))
print(koyama(3))
print(koyama(0))
print(koyama(4))


