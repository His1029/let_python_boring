import random

def get_answer(answer_number):
    if answer_number == 1:
        return '少佐'
    elif answer_number == 2:
        return 'バトゥ'
    elif answer_number == 3:
        return 'トグサ'
    elif answer_number == 4:
        return 'イシカワ'
    elif answer_number == 5:
        return 'サイトウ'
    elif answer_number == 6:
        return 'タチコマ'

i = random.randint(1,6)
kokaku = get_answer(i)
print(i,end=' ')
print(kokaku)


