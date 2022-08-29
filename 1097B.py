n = int(input())

my_list = list()
for i in range(0, n):
    my_list.append(int(input()))

flag =False
for i in range(0, pow(2,n-1)):
    my_bin = bin(i)

    my_help_bin ='0'*(n-len(my_bin)+2)+ my_bin[2::]

    sum = my_list[0]
    j = 1
    while j<n:
        b = my_help_bin[j]
        if b=='0':
            sum+=my_list[j]
        else:
            sum-=my_list[j]

        j += 1

    if sum%360==0:
        flag = True
        break

if flag == True:
    print("YES")
else:
    print('NO')

