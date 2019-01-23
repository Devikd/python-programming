v,d=map(int,input().split())
arr=input().split()
l=[]
for y in arr:
l.append(int(y))
l.sort()
for y in range(0,len(l)):
    if(d==l[y]):
    if(y==0):
 print(l[y+1],l[y+2],l[y+3],sep=' ')
   if(x==len(l)-1):
 print(l[y-1],l[y-2],l[y-3],sep=' ')
    if(y>1 and y<len(l)-2):
print(l[y-1],l[y+1],l[y-2],sep=' ')
    if(y==1):
 print(l[y-1],l[y+1],l[y+2],sep=' ')
