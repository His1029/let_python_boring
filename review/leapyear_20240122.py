def leapyear(year:int):
    if year % 400 == 0 :
        print("うるう年")
    else:
        print("平年")

year = 400
print(year,end = ' : ')
leapyear(int(year))