import re
phone_num_regex = re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
mo = phone_num_regex.findall('私の電話番号は090-9312-0655です。彼女の電話番号は090-5101-1727です。')
print(mo if mo else '電話番号は見つかりませんでした')
