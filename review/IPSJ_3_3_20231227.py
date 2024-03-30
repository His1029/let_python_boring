yokin = [6550000]*11
riritsu = 0.048
for i in range(10):
    risoku = yokin[i]*riritsu
    yokin[i + 1] = yokin[i] + risoku
    print(i+1,' 年目 : ', yokin[i+1])