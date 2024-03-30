cat_names = []

while True:
    print('猫' + str(len(cat_names)+1) + 'の名前を入力してください' + '(終了するにはenterキーを押してください)')
    name = input()
    cat_names = cat_names + [name]
    if name == '':
        break      
print('猫の名前は次の通り：')
for name in cat_names :
    print(' ' + name,end = '')

          