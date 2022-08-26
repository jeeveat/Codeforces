t = int(input())

for i in range(0, t):

    n = int(input())

    s = input()

    numb1 = n-1
    flag = False
    while numb1>=0:
        if s[numb1]=='0':
            break
        numb1 -= 1


    numb2 = 0
    flag = False
    while numb2<n:
        if s[numb2]=='1':
            break
        numb2 += 1
    if numb2>numb1:
        print(s)
    else:
        print(s[0:numb2]+s[numb1:n]) 
