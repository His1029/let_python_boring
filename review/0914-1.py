#猫の名前を連続で入力し、空白の場合にはそれまで入力したものを羅列する
cat_names = []#初期化されたリスト
while True:
    print('猫' + str(len(cat_names) + 1) + 'の名前を入力してください\n' + '(終了するにはEnterキーを入力してください)')
    name = input()#inputは組込関数
    if name == '':
        break
    cat_names += [name]#ここまではwhileの中
print('猫の名前は以下の通り:')#whileの外
for name in cat_names:#forループ
    print(name)



