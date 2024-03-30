def spam(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:
        return('0除算が発生しました')

print(spam(2))
print(spam(3))
print(spam(10))
print(spam(0))