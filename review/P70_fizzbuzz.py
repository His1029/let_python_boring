for i in range(1,31):
    if i % 15 == 0:
        print(i,end = ': ')
        print('fizzbuzz')
    elif i % 3 == 0:
        print(i,end = ': ')
        print('fizz')
    elif i % 5 == 0:
        print(i,end = ': ')
        print('buzz')
    else :
        print(i)
        
