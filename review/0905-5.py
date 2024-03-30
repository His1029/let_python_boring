import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'Love'
    elif answer_number == 2:
        return 'and'
    elif answer_number == 3:
        return 'Peace'

r = random.randint(1,3)
print(r)
fortune = get_answer(r)
print(fortune)
