s,n = map(int, input().split())
my_list = list(map(int, input().split()))

my_list.sort()
help_list=[1]
num = 0
elem = -1
for i in range(1,len(my_list)):
    if elem==my_list[i]:
        help_list[len(help_list)-1]+=1
    else:
        help_list.append(help_list[len(help_list)-1]+1)
        elem = my_list[i]
    
#print(help_list)

flag = 0
if n in help_list:
    ind = help_list.index(n)
else:
    ind = -1
if ind!=-1:
    flag = 1

if flag ==0:
    print(-1)
else:
    print(my_list[help_list[ind]-1])
