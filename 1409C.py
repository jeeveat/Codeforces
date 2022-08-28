for i in range(int(input())):

    n,x,y = map(int,input().split())

    my_list = list()

    count = 0
    for elem in range(1,y-x+1):
        if (y-x)%elem==0:
            if (y-x)//elem <= n-1:
                count =elem
                break

    number_of_elem = n
    help_elem = y
    while number_of_elem>0:
        my_list.append(help_elem)
        help_elem -= count
        number_of_elem-=1
        if help_elem<=0:
            break

    if number_of_elem!=0:
        help_elem = y+count
        while number_of_elem>0:
            my_list.append(help_elem)
            help_elem += count
            number_of_elem-=1

    for elem in my_list:
        print(elem,end=" ")
    print()

    

