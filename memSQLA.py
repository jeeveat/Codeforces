s = input()
n = int(input())
my_list = list()
my_set = set()
for elem in s:
    if elem not in my_set:
        my_list.append([elem,1])
        my_set.add(elem)
    else:
        ind = 0
        while ind<len(my_list):
            if elem == my_list[ind][0]:
                break
            ind += 1
        my_list[ind][1] += 1

help_list=[1 for i in range(0, len(my_list))]

max_ = 0
r = n - len(my_list)
if n<len(my_list):
    print(-1)
else:
    ind = 0
    while ind<r:
        max_ = 0
        for i,elem in enumerate(help_list):

            m = my_list[i][1]//help_list[i]
            if my_list[i][1]%help_list[i]!=0:
                m += 1
            if m>max_:
                max_ = m
                my_index = i
        help_list[my_index] += 1

        ind += 1

    max_ = 0
    s = ""
    for i,elem in enumerate(help_list):
        s += elem * my_list[i][0]
        m = my_list[i][1]//help_list[i]
        if my_list[i][1]%help_list[i]!=0:
            m += 1
        if m>max_:
            max_ = m

    print(max_)
    print(s)