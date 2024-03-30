def listgoukei(a):
    goukei = 0
    for i in range(0,len(a),1):
        goukei = goukei + a[i]
    return goukei

a = [1,27,29,55,7,4,0,16,19,142]
goukei = listgoukei(a)
print(len(a))
print(a)
print(goukei)
print(a[0])
print(a[5])
print(a[9])