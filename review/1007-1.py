def spam(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:
        return('0除算が発生しました')
    except TypeError:
        return('文字で割りました')

print(spam(42))
print(spam(40))
print(spam(0))
print(spam('string'))