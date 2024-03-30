public_items = {'apples': 5,'oranges':10}

print('------------apples----------------')
print('I am bringing',end= ' ')
print(public_items.get('apples', 0),end = ' ')
print('apples.')

print('------------oranges----------------')
print('I am bringing',end= ' ')
print(public_items.get('oranges', 0),end = ' ')
print('oranges.')
