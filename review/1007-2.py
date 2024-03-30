def eggs(same_parameter):
    same_parameter.append('Hello')

spam = [1,2,3]
eggs(spam)
print(spam)