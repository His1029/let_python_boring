import random
def get_answer(answer_number):
    if answer_number == 1:
        return 'ウルトラマン'
    if answer_number == 2:
        return '帰ってきたウルトラマン'
    if answer_number == 3:
        return 'ウルトラマンセブン'
    if answer_number == 4:
        return 'ウルトラマンエース'
    if answer_number == 5:
        return 'ウルトラマンタロウ'
    if answer_number == 6:
        return 'ウルトラマンレオ'
    if answer_number == 7:
        return 'ウルトラマン８０'
    if answer_number == 8:
        return 'ザ・ウルトラマン'
    
r = random.randint(1,8)
print(r)
fortune = get_answer(r)
print(fortune)
    