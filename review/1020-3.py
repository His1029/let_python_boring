import sys

while True:
    print('終了するにはexitと入力してください')
    response = input()
    if response == 'exit':
        sys.exit('終了します')
    print(response + 'と入力されました')


