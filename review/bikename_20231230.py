import random

def bike(name) :
    if name == 1:
        return 'YZF-R25'
    elif name == 2:
        return 'MT-25'
    elif name == 3:
        return 'ZX-25R'
    elif name == 4:
        return 'Ninjya250'
    elif name == 5:
        return 'GSX-250R'
    elif name == 6:
        return 'CBR250RR'
    elif name == 7:
        return 'NS250R'
    elif name == 8:
        return 'Γ250'
    elif name == 9 :
        return 'TZR250'

name = random.randint(1,9)
mortorcycle = bike(name)
print(name,end = ' ')
print(mortorcycle)
