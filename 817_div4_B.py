for i in range(int(input())):

    n = int(input())

    s1 = input()
    s2 = input()

    flag = True
    for k in range(0, n):
        if (s1[k] != s2[k]) & ((s1[k]=='R')|(s2[k]=='R')):
            flag = False

    if flag == True:
        print("YES")
    else:
        print("NO")
