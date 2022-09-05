n, k = map(int, input().split())

a = list(map(int, input().split()))

sum = 1
koef = 1
for i in range(n-1,0,-1):
    if a[i-1]!=a[i]:
        koef += (n-i)
    koef += 1
    sum +=koef

#print(sum)
for j in range(0, k):
    
    ind, elem = map(int, input().split())
    ind -= 1
    pred_elem = a[ind]
    a[ind] = elem
    if pred_elem == elem:
        print(sum)
    else:
        sum1 = 0
        sum2 = 0
        if ind>0:
            el = a[ind-1]
            if elem == el:
                sum1 -= (n-ind)*(ind)
            elif pred_elem == el: 
                sum1 += (n-ind)*(ind)
        if ind<n-1:
            el = a[ind+1]
            if elem == el:
                sum2 -= (n-ind-1)*(ind+1)
            elif pred_elem == el: 
                sum2 += (n-ind-1)*(ind+1)
        sum+= sum1+sum2
        print(sum)


