import re
hero_regex = re.compile(r'Batman|Joker')
print('\n----mo-----')
mo = hero_regex.search('Batman VS Joker.')
print(mo.group())
print('\n----mo1-----')
mo1 = hero_regex.search('Batman VS Joker.')
print(mo1.group())
print('\n----mo2-----')
mo2 = hero_regex.search('Joker VS Batman.')
print(mo2.group())
