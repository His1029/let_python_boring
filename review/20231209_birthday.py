birthdays = {'ゆき':'1/19','ひさし':'10/29','じーじ':'8/31'}

while True:
    print('名前を入力して。終了の場合はEnterキー押して')
    name = input()

    if name == '':
        break

    if name in birthdays:
        print(name + 'の誕生日は' + birthdays[name])

    else:
        print(name + 'の誕生日は未登録です' )
        print('誕生日を登録しましょう')
        bday = input()
        birthdays[name] = bday
        print(birthdays[name])
        print(birthdays)
        print('誕生日を登録しました')