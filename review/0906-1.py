import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'yamada'
    elif answer_number == 2:
        return 'murakami'
    elif answer_number == 3:
        return 'nakamura'

print(get_answer(random.randint(1,3)))
