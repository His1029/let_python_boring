import pyinputplus as pyip

while True:
    age = input('年齢を入力してください')
    try:
        age = int(age)
        
    except:
        print('数字を入力してください:')
    
    
    if age < 0:
        print('0以上の数字を入力してください')
    
    break

print(f'あなたの年齢は{age}です')
    