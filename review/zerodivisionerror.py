def spam(divide_by): #42をdivide_byで割る関数の設定
    try: # ゼロ除算をはじく前設定
        return 42 / divide_by
    except ZeroDivisionError :  # ゼロ除算をはじく後設定
        print('ゼロで割ったらあかんよ')

# ----メインプログラムだっちゃ---------------
print(spam(42))
print(spam(21))
print(spam(14))
print(spam(0))
