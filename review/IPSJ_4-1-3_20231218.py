a = [82,28,56,78,100,98,56,44,62]
for i in range(0,10,1):
    if a[i] >= 90:
        print(str(a[i]) + ': S')
    elif a[i] >= 80:
        print(str(a[i] ) + ': A')
    elif a[i] >= 70:
        print(str(a[i] ) + ': B')
    elif a[i] >= 30:
        print(str(a[i] ) + ': C')
    else:
        print(str(a[i] ) + ': X')
    