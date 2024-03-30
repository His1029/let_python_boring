Y = [1,4,9,16,18,19,29,34,55,67,88]
saidai = Y[0]
for i in range(1,11):
    if Y[i] > saidai:
        saidai = Y[i]
print(saidai)