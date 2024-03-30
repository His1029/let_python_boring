while True:
    print('あなたの名前は何ですか')
    print('名前:',end='')
    name = input()
    if name != 'koyama' :
        continue
    print('こんにちわ。パスワードを入力してください')
    print('パスワード:',end='')
    password = input()
    if password == 'password':
        break
print('認証しました')