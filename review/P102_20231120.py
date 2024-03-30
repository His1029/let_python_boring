cat_names = []
while True:
    print('猫' + str(len(cat_names)+1) + 'の名前を入力してください' + '(終了するにはEnterキーを入力してください)')
    name = input('猫の名前:')
    cat_names += [name]
    if name == '':
        break
print('猫の名前は次の通り:')
for name in cat_names:
    print(' ' + name)

