def listgoukei(a):
    goukei = 0
    for i in range(0,len(a),1):
        goukei = goukei + a[i]
    return goukei
    
a = [1,27,29,19,17,18,47,55,87]
goukei = listgoukei(a)
print(goukei)