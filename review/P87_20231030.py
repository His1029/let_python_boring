def momo(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        return('0で割らないで')

print(momo(2))
print(momo(3))
print(momo(0))
print(momo(6))