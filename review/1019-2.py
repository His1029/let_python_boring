name = ''
while not name :
     print('名前を入力してください')
     name = input('名前:')

print('同伴者は何人ですか')
try:
    guests = int(input('人数:'))
    if guests == 0:
        print('あなたの席を確保しました')
    elif guests != 0 :
        print('同伴者の席の確保お願いします')
    
    
except:
    print('数値を入力してください')

