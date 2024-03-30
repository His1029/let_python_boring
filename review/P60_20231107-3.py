for i in range(1,31):
    print(i,end = ':')
    if i % 3 == 0:
        print('fizz',end ='')
    if i % 5 == 0:
        print('buzz',end ='')
    print()
