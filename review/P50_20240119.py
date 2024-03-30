while True:
    print('あなたの名前を入力してください')
    print('名前:' ,end='')
    name = input()
    if name != 'koyama':
        continue
    print('こんにちわ。' + name + 'さん、続けてパスワードを入力してください')
    print('パスワード:',end ='')
    password = input()
    if password == 'password':
        break
print('認証しました')