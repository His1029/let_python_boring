def leapyear(year):
    if year % 400 == 0:
        print('うるう年')
    else:
        print('平年')
        
#-------------メインプログラム----------------

while True:
    try:
        print('西暦を入力してください',end =':' )
        year = input()
        leapyear(int(year))
        break
    except:
        print('数値を入力してください')

print('終了！')