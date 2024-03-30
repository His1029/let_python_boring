# 無限ループを発生させる
while True:
    print('あなたは誰ですか')
    name = input("名前:")
    if name == '':
        continue
    else:
        print(name + 'さん、こんにちわ！')
        break

print('ようこそ！')
    
    