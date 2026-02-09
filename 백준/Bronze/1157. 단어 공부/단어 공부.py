# 1157번
s = input().upper()
l=[]
s_list = list(set(s))

for i in s_list:
    l.append(s.count(i))
    
if l.count(max(l)) != 1:
    print("?")
else:
    print(s_list[l.index(max(l))])