def pita(divide):
    try:
        return 100 / divide
    except:
        return 'ゼロ除算はできません。'

print(pita(1))
print(pita(2))
print(pita(4))
print(pita(5))
print(pita(6))
print(pita(10))
print(pita(0))
    
    