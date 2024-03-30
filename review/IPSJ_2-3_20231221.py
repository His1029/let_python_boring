import datetime

now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
h = now.hour

if h <= 3 or h == 23:
    print('おやすみなさい')
elif h <= 9:
    print('おはよう')
elif h <= 16:
    print('こんにちわ')
else:
    print('こんばんわ')
    