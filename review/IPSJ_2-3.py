import datetime
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
h = now.hour
print(h , '時')
if h <= 4 or h == 23 :
    print('おやすみ')
elif h <= 10 :
    print('おはよう')
elif h <= 16 :
    print('こんにちわ')
else :
    print('こんばんわ')


