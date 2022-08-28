
for i in range(int(input())):
    n = int(input())

    my_list = list(map(int,input().split()))

    my_list.sort()

    sum_Alice = 0
    sum_Bob   = 0
    j = 0
    i = n-1
    while i>=0:
        elem = my_list[i]

        if j%2:
            if elem%2:
                sum_Bob += elem
        else:
            if elem%2==0:
                sum_Alice += elem
        j += 1
        i -= 1

    if sum_Alice>sum_Bob:
        print("Alice")
    elif sum_Alice<sum_Bob:
        print("Bob")
    else:
        print("Tie")
        


