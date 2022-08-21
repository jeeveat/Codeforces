from stringprep import in_table_d1


t = int(input())

for i in range(0, t):

    s = int(input())
    my_list = list(map(int, input().split()))
    #help_list=list(my_list[])


    pos = len(my_list)-1

    while (pos>0) & (my_list[pos-1]>=my_list[pos]):
        pos -= 1

    while (pos>0) & (my_list[pos-1]<=my_list[pos]):
        pos -= 1
       
    print(pos)

