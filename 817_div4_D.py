for i in range(int(input())):

    n = int(input())

    s = (input())

    sum = 0
    for i, elem in enumerate(s):
        if elem=='R':
            sum += n-i-1
        else:
            sum += i

    my_list = [0 for j in range(0, n)]
    sum1 = sum
    for i in range(0,len(s)//2):
        sum1 = 0
        elem = s[i]

        if elem =='L':
            sum1 += n-2*i-1
        my_list[i]=(sum1)
        

    for i in range(len(s)//2,len(s)):
        elem = s[i]
        sum1 = 0
        if elem =='R':
            sum1 += 2*i-n+1
            my_list[i]=(sum1)

    my_list.sort()
    k = 0
    while (my_list[k]<=0) & (k<n):
        k += 1
        if k==n:
            break

    k1 = k
    for j in range(n-1, k-1,-1):
        sum +=my_list[j]
        print(sum, end=" ")

    for j in range(0, k1):
        print(sum, end=" ")

    






