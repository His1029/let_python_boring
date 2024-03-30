cat_names = []
while True:
    print('猫'+ str(len(cat_names) + 1) + 'の名前を入力してください' + '(終了するにはEnterキーを入力してください)')
    name = input()
    if name == '':
        break
    else:
        cat_names = cat_names + [name]
print('猫の名前は次のとおり:')
for name in cat_names:
    print('' ,name,end='')