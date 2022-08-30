for i in range(int(input())):

    n = int(input())
    my_list = list()
    #help_list = [[-1] for j in range(0, 1001)]
    help_list = list()
    for j in range(0, n):
        x, y = map(int,input().split())
        my_list.append([x,y])
        
        if len(help_list)==0:
            help_list.append([x,y])
        else:
            k = 0
            while (k<len(help_list)) :
                if (x<=help_list[k][0]):
                    break
                k += 1
            
            while (k<len(help_list)):
                if (y<=help_list[k][1]):
                    break
                k += 1
            
            if k == len(help_list):
                help_list.append([x,y])
            else:
                help_list.insert(k,[x,y])

    flag = True

    for j in range(0,n):

        for k in range(0, n):

            if (my_list[j][0]<my_list[k][0]) & (my_list[j][1]>my_list[k][1]):
                flag = False
                break

        if flag==False:
            break

    if flag == False:
        print("NO")
    else:
        s=""
        current_x = 0
        current_y = 0

        for elem in help_list:
            x = elem[0]
            y = elem[1]
            s += 'R'*(x-current_x)+'U'*(y-current_y)
            current_x = x
            current_y = y

        print("YES")
        print(s)


