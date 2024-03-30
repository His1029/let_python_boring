# うるう年判定を行う関数
def leapyear(year:int):
    
    # 引数で受け取った変数の値でうるう年判定を行う
    if year % 2000== 0:
        # 2000で割り切れる場合
        return '平年'
    elif year % 2400== 0:
        # 2400で割り切れる場合
        return '平年'
    elif year % 4 == 0:
        # 4で割り切れる場合
        return 'うるう年'
    elif year % 100 == 0:
        # 100で割り切れる場合
        return '平年'
    elif year % 400== 0:
        # 4で割り切れる場合
        return 'うるう年'
    else:
        # それ以外はうるう年ではない
        return '平年'
    
#------------------- メインプログラム --------------------#

while True:
    print('---うるう年判定を行います---')
    print('西暦を入力してください（未入力でEnterキーを押すと終了できます）')
    
    # キーボード入力を変数で受け取る
    year = input()
    
    # キーボードから入力された値が空文字であれば、ループを抜ける
    if year == '':
        break
    
    # 戻り値（うるう年判定の結果を出力する）
    #print(str(year) + ' は ' + leapyear(int(year)))
    
    print(str(year),end = ':')
    print(leapyear(int(year)))
    
print('未入力のため、終了します')