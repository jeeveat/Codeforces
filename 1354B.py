t = int(input())
 
for i in range(0, t):
 
    s = input()
    min_ = 1000000
 
    my_list = list([s[0]])
 
    x1 = 0
 
    for j in range(0,len(s)-1):
        el = s[j+1]
 
 
        if el not in my_list:
            my_list.append(el)
        if len(my_list)==3:
            if min_>j-x1+2:
                min_ = j-x1+2
 
            x1=j
            my_list.pop(0)
 
        if s[j]!=s[j+1]:
            my_list[0]=s[j]
            my_list[1]=s[j+1]
            x1=j
 
 
    if min_==1000000:
        print(0)
    else:
        print(min_)