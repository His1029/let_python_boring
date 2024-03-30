# 奇遇判定を行う関数
def JudgmentOfChance(num:int):
    # 判定結果を詰め込む変数を用意する(ansの初期化)
    #ans = ''
    
    # 引数で受け取った変数の値で奇遇判定を行う
    if num % 2 == 0:
        # 偶数の場合
        #ans = '偶数'
        return '偶数'
    else:
        # 奇数の場合
        #ans = '奇数'
        return '奇数'
    # 判定結果を呼び出し元に返却する
    #return ans

#------------------- メインプログラム --------------------#

while True:
    print('---奇数・偶数判定を行います---')
    print('数値を入力して下さい（未入力でEnterキーを押すと終了できます）')
    
    # キーボード入力を変数で受け取る
    num = input()
    
    # キーボードから入力された値が空文字であれば、ループを抜ける
    if (num == ''):
        break
    
    # 受け取った変数を引数として、関数『JudgmentOfChance』を呼び出す
    #ans = JudgmentOfChance(num)
    
    # 戻り値（奇遇判定の結果を出力する）
    #print(str(num) + ' は ' + JudgmentOfChance(int(num)) + 'です')
    
    print(str(num) + ' は ' + JudgmentOfChance(int(num)))