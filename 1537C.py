for i in range(int(input())):
    n = int(input())

    my_list = list(map(int, input().split()))

    my_list.sort()
    
    min_ = 100
    number = -1
    for j in range(1,n):
        if min_>(my_list[j]-my_list[j-1]):
            min_ = (my_list[j]-my_list[j-1])
            number = j

    if n >2:
        for k in range(number,n):
            print(my_list[k],end=" ")

        for k in range(0,number):
            print(my_list[k],end=" ")
    else:
        print(my_list[0],end=" ")
        print(my_list[1],end=" ")

    print()

    


