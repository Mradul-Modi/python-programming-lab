num=[1,2,3,3,4,2,5,6,7,5,6]
a=[]
for i in range(len(num)):
    if num[i]not in a:
        a.append(num[i])
    else:
        pass
print(a)
