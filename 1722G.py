for t in range(0, int(input())):

    n = int(input())
    if n%4!=0:
        r = 1
    else:
        r = 0
    if (n%4== 0) | (n%4==3):
        number = 5
        for i in range(0, n//4-1+r):
            print(number, number-1,number + 2, number+1, end=" ")
            number += 4
        if n%4==0:
            print(2,1,3,0)
        else:
            print(2,1,3)
    else:
        number = 5
        for i in range(0, n//4):
            if number == 5:
                print(pow(2,30)+number,number - 1,number+2,number+1,end=" ")
            else:
                print(number, number-1,number + 2, number+1, end=" ")
            number += 4
        if n%4==2:
            print(pow(2,30),0)
        else:
            print(pow(2,30))
        

