import random

def get_answer(answer_number):
    if answer_number == 1:
        return 'YZF-R25'
    elif answer_number == 2:
        return 'ZX-25R'
    elif answer_number == 3:
        return 'GSX-250R'
    elif answer_number == 4:
        return 'CBR250RR'
    elif answer_number == 5:
        return 'Ninjya 250'
    
name = random.randint(1,5)
BIKE = get_answer(name)
print(BIKE,end = ' : ')
print(name)