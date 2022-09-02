for k in range(int(input())):

    n, q = map(int, input().split())

    my_map =list()

    a = [[0]*1001 for _ in range(1001)]

    for j in range(0, n):
        h_i, w_i = map(int, input().split())
        a[h_i][w_i] += h_i * w_i 


    for i in range(1, 1001):
        for j in range(1,1001):         
            a[i][j] += a[i-1][j]+a[i][j-1]- a[i-1][j-1]


    for z in range(0, q):
        sum = 0

        h_s,w_s,h_b,w_b = map(int, input().split())
    

        print(a[h_b-1][w_b-1]-a[h_b-1][w_s]-a[h_s][w_b-1]+a[h_s][w_s])

    

