import random

def get_answer(answer_number):
    if answer_number == 1:
        return("ガンダム")
    elif answer_number == 2:
        return("ザク")
    elif answer_number == 3:
        return("ガンキャノン")
    elif answer_number == 4:
        return("ガンタンク")
    elif answer_number == 5:
        return("ジーアーマー")
    elif answer_number == 6:
        return("ドム")
    elif answer_number == 7:
        return("ゲルググ")   

r = random.randint(1,7)
print(r)
print(get_answer(r))
    