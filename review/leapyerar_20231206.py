def leapyear(year:int):
    if year % 400 == 0:
        print('うるう年')
    else:
        print('平年')
    

while True:
    try:
        print('西暦を入力してください')
        year = input('西暦:')
        leapyear(int(year))
        break
    except:
        print('西暦(4桁の数値)を正しく入力してください')

print('終了')

   