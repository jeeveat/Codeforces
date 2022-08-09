n = int(input())

#n = int(input())

v = list(map(int, input().split()))

v_sorted = sorted(v)

my_list=[]
sorted_list=[]
sum_ = 0
sum__ = 0



for i in range(0, n):

    sorted_list.append(sum__)
    my_list.append(sum_)
    sum_ += v[i]
    sum__+= v_sorted[i]
    
sorted_list.append(sum__)
my_list.append(sum_)

m = int(input())

for i in range(0, m):
    
    my_type,l,r = map(int, input().split())

    if my_type==1:
        print(my_list[r]-my_list[l-1])
    else:
        print(sorted_list[r]-sorted_list[l-1])
        
