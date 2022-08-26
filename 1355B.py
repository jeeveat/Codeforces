t = int(input())

for i in range(0, t):

    n = int(input())

    my_list = list(map(int, input().split()))

    my_list.sort()

    count = 0
    numb_of_el = 1
    for j in range(0, n):
        if numb_of_el>=my_list[j]:
            numb_of_el = 1
            count += 1
        else:
            numb_of_el += 1
    print(count)

