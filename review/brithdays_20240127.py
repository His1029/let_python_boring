birthdays = {'小山':'1/19','中山':'10/29'}

while True:
    print('名前を入力してください。終了するにはenterキーを押してください') #名前の入力促進
    name = input() #名前の入力
    
    if name == '':
        break
    
    elif name in birthdays:
        print(name + 'の誕生日は' + birthdays[name])
    
    else:
        print(name + 'の誕生日は未登録です') #未入力の名前の場合の入力支援
        print('誕生日を登録しましょう') #未入力の名前の場合の入力支援
        bday = input() #未入力の誕生日をvalue値として登録
        birthdays[name] = bday #birthdaysの辞書の変数に未登録の誕生日を登録
        print(birthdays)
        

print('enterキーが押されたので終了します')
        
    