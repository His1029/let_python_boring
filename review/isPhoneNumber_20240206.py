def is_phone_number(text):
    if len(text) != 13:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False 
    for i in range(4,8):
        if not text[i].isdecimal():
            return False  
    if text[8] != '-':
        return False
    for i in range(9,13):
        if not text[i].isdecimal():
            return False
    return True
    
        
print('03-3333-5555は携帯番号に相当しますか?')
print(is_phone_number('03-3333-5555'))

message = '明日090-9312-0655に電話してください。会社は080-4414-6361です'
for i in range(len(message)):
    chunk = message[i:i+13]
    if is_phone_number(chunk):
        print('電話番号が見つかりました！: ' + chunk)
print('完了')
