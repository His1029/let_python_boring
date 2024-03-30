birthdays = {'1/19':'桃山','10/29':'小山'}

while True:
    print('誕生日を入力してください。終了するにはenterキーを押してください') #誕生日の入力促進
    bday = input() #誕生日の入力
    
    if bday == '':
        break
    
    elif bday in birthdays:
        print(bday + 'の名前は' + birthdays[bday])
    
    else:
        print(bday + 'の名前は未登録です') #未入力の名前の場合の入力支援
        print('名前を登録しましょう') #未入力の名前の場合の入力支援
        name = input() #未入力の名前をkeyとして登録
        birthdays[bday] = name #birthdaysの辞書の変数に未登録の名前を登録
        print(birthdays)
        

print('enterキーが押されたので終了します')