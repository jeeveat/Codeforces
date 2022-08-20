s = input()
s1=""
#if s[0]=='9'| int(s[0])>4:
if s[0]=='9':
        s1+=s[0]
elif int(s[0])<5:
    s1+=s[0]
else:
    s1+=str(9-int(s[0]))
for el in s[1:]:
    if int(el)>4:
        s1+=str(9-int(el))
    else:
        s1+=el

print(s1)
