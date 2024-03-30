import sys

while True:
    print('終了するためにexitと入力してください。:',end ='')
    response = input()
    if response =='exit':
        sys.exit('終了')
    elif response != 'exit':
        print('exitではなく' + response + 'と入力されました。')


    
        
    