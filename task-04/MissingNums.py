n=int(input())
a=list(input().split(" "))
m=int(input())
b=list(input().split(" "))
x=[]
for i in b:
    if a.count(i)!=b.count(i):
        x.append(i)
print(*set(x),sep=" ")
