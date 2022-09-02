for i in range(int(input())):

    n = int(input())

    sum1 = 0
    sum2 = 0
    sum3 = 0 
    s_one  = list(map(str,input().split()))
    s_two  = list(map(str,input().split()))
    s_three = list(map(str,input().split()))

    s_one_list = set(s_one)
    s_two_list = set(s_two)    
    s_three_list = set(s_three)

    for k in range(0, n):
        s1 = s_one[k]
        s2 = s_two[k]
        s3 = s_three[k]

        if (s1 not in s_two_list) & (s1 not in s_three_list):
            sum1 += 3

        if (s2 not in s_one_list) & (s2 not in s_three_list):
            sum2 += 3

        if (s3 not in s_two_list) & (s3 not in s_one_list):
            sum3 += 3

        if(s1 in s_three_list) & (s1 not in s_two_list):
            sum1+=1
        if(s1 in s_two_list) & (s1 not in s_three_list):
            sum1+=1       

        if (s2 in s_one_list) & (s2 not in s_three_list):
            sum2+=1
        if (s2 in s_three_list) & (s2 not in s_one_list):
            sum2+=1


        if (s3 in s_one_list) & (s3 not in s_two_list):
            sum3+=1
        if (s3 in s_two_list) & (s3 not in s_one_list):
            sum3+=1 

    print(sum1,sum2,sum3)      
                
        

