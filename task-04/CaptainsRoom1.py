n=int(input())
roomlist=list(input().split())
for i in roomlist:
    if roomlist.count(i)==1:
        print(i)
        break