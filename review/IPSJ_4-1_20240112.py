a = [1,27,55,29,67,81,99,47,16]

for i in range(0,9,1):
    if a[i] >= 90:
        print(str(a[i])+':S')
    elif a[i] >= 80:
        print(str(a[i])+':A')
    elif a[i] >= 70:
        print(str(a[i])+':B')
    elif a[i] >= 60:
        print(str(a[i])+':C')
    elif a[i] >= 50:
        print(str(a[i])+':D')
    else:
        print(str(a[i])+':X')