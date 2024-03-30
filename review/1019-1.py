name = ''
while not name :
    print('名前を入力してください')
    name = input('名前:')
print('同伴者は何人ですか')
try:
 num_of_guests = int(input('人数:'))
 if num_of_guests == 0 :
    print('同伴者なし、1名様で受け付けました')
 elif num_of_guests != 0 :
    print('同伴者用の座席も確保ください')
 ##elif num_of_guests == '' :
   ## print('人数を入力してください。同伴者がいなければ０で入力お願いします')
except :
   print('人数を入力してください。同伴者がいなければ０で入力お願いします')





 

