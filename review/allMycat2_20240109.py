cat_names = [] #リストの初期化
while True:
    print('サザエさん一家' + str(len(cat_names)+1) + 'の名前を入力してください' + '(終了するにはEnterキーだけを入力してください)')
    name = input('サザエさん一家の名前:')
    cat_names += [name] #リストの連結
    if name == '':
        break

'---------------breakの先---------------------'
print('サザエさん一家の名前は次の通りです。:')
for name in cat_names:
    print(name,end=' ')    