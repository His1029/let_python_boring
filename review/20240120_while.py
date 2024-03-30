name = ''
while not name :
    print('名前を入力してください') #入力補助
    print('名前:',end = '') #入力補助_改行なし
    name = input()
print('同伴者は何人ですか?') #入力補助
try:
    print('人数:',end = '') #入力補助_改行なし
    num_of_guest = int(input()) 
    if num_of_guest == 0 :
        print('同伴者様なし、1名様で受け付けました')
    elif num_of_guest != 0 :
        print('同伴者様の席も確保ください')
except:
    print('人数を入力してください。同伴者がいなければ0でご入力お願いします。')