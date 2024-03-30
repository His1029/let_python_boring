while True:
    print('あなたは誰ですか')
    name = input()
    if len(name)==0:
        continue
    else:
        print(name + 'さん、こんにちわ！')
        break

