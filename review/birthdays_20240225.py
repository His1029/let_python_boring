birthdays = {'桃山':'1/19','小山':'10/29'}

while True:
    print('名前を入力してください。終了するにはenterキーを押してください') #名前の入力促進
    bname = input() #名前の入力
    
    if bname == '':
        break
    
    elif bname in birthdays:
        print(bname + 'の誕生日は' + birthdays[bname])
    
    else:
        print(bname + 'の誕生日は未登録です') #未入力の誕生日の場合の入力支援
        print('誕生日を登録しましょう') #未入力の誕生日の場合の入力支援
        bday = input() #未入力の誕生日をkeyとして登録
        birthdays[bname] = bday #birthdaysの辞書の変数に未登録の誕生日を登録
        print(birthdays)
        

print('enterキーが押されたので終了します')