for i in range(int(input())):

    n = int(input())

    s = input()
    my_list = ['T','i','m','u','r']
    help_list=[0 for k in range(0, 5)]
    flag = True

    if n!=5:
        flag = False

    for elem in s:
        if elem not in my_list:
            flag = False
            break
        else:
            ind = my_list.index(elem)
            help_list[ind] += 1
            if help_list[ind]>1:
                flag = False
                break


    if flag == True:
        print("YES")
    else:
        print("NO")

