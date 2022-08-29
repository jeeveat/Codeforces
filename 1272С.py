n, k = map(int, input().split())

s = input()

my_set = set(map(str, input().split()))
i = 0
sum = 0
for j,elem in enumerate(s):
    if (elem not in my_set):
        sum += int(i*(i+1)*0.5)
        i = -1
    elif (j==len(s)-1):
        i += 1
        sum += int(i*(i+1)*0.5)
    i += 1

print(sum)


