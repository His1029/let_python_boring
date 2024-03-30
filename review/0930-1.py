import random

def get_answer(answer_number):
    if answer_number == 1:
        print('ウルトラマン')
    elif answer_number == 2:
        print('帰ってきたウルトラマン')
    elif answer_number == 3:
        print('ウルトラマンセブン')
    elif answer_number == 4:
        print('ウルトラマンコスモス')
    elif answer_number == 5:
        print('ウルトラマンエース')
    elif answer_number == 6:
        print('ウルトラマンタロウ')
    elif answer_number == 7:
        print('ウルトラマン８０')

p = random.randint(1,7)
print(p)
specium = get_answer(p)
print(specium)