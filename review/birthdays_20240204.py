#birthdays = {'大山':'1/19','小山':'10/29'}
birthdays = {'1/19':'大山','10/29':'小山'}

while True:

    print('名前を入力してください。終了するにはenterキーを押してください') #誕生日の入力促進
    name = input() #名前の入力
    
    if name ==  '':
        break
    else:
      flg = False  
      for bday in birthdays:
        if birthdays[bday] == name:         
            print(name + 'の誕生日は' + bday)
            flg = True
            break # forのブレイク
        
      if flg == True: # 見つかった時
        break # whileのbreak
      else: # 見つからなかった時
          print(bday + 'の名前は未登録です') #未入力の名前の場合の入力支援
          print('名前を登録しましょう') #未入力の名前の場合の入力支援
          name = input() #未入力の名前をkeyとして登録
          birthdays[bday] = name #birthdaysの辞書の変数に未登録の名前を登録

print(birthdays)