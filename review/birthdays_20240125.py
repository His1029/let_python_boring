birthdays = {'アリス':'4/1','キャロル':'4/2'}  #辞書リスト

while True:
    print('名前を入力してください。終了するにはenterキーを押して下さい') #入力補助
    name = input() #名前の入力
    
    if name == '':  #未入力の場合は無限ループを抜けて終了
        break

    elif name in birthdays:
        print(name + 'の誕生日は' + birthdays[name] )
    
    else:
        print(name + 'は未登録の名前です') #入力補助
        print('名前は頂いたので、誕生日を入力してください。登録します')
        bday = input() #誕生日の入力
        birthdays[name] = bday #[]辞書リストを用いてキーの名前にバリューの誕生日を追加。キーバリューペアの一組が完成
        print(birthdays)
    
    
    
print('enterキーが押されたので終了します')