for i in range(int(input())):
    n = int(input())

    s = input()
    if len(s)>1:
        if  (len(s)%2==1)&(s[len(s)//2]=='0'):

            if s.count('0')==1:
                print("BOB")
            else:
                print("ALICE")
        else:
            print("BOB")
    else:
        print("BOB")