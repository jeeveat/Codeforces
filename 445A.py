n, m = map(int, input().split())

for i in range(0, n):
    s = input()

    for j, elem in enumerate(s):
        if elem=='.':
            if (i+j)%2 == 0 :
                print('B',end="")
            else:
                print('W',end="")
        else:
            print('-',end="") 
    print()





