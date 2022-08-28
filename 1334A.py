for i in range(int(input())):
    n = int(input())

    flag = True
    p_prev, c_prev = map(int,input().split())
    if(p_prev<c_prev):
        flag=False
    for j in range(1, n):
        p, c =  map(int,input().split())
        if(p_prev>p)|(c_prev>c)|(p<c)|(p-p_prev<c-c_prev):
            flag = False
        p_prev = p
        c_prev = c

    if (flag == False):
        print("NO")
    else:
        print("YES")
