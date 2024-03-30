def judgementofchance(num):
    ans =''
    if num % 2 == 0:
        ans = '偶数'
    else:
        ans = '奇数'
    return ans


num = 100
ans = judgementofchance(num)
print(num)
print('判定は' + ans + 'です')