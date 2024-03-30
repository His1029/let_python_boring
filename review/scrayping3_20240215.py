import re
phone_num_regex = re.compile(r'\d\d-\d\d\d\d-\d\d\d\d')
mo = phone_num_regex.findall('03-6890-2540')
print(mo if mo else '電話番号は見つかりませんでした')