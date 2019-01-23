def repeat(d,k,i):
  d=[]
  for i in range(k):
    flag=0
    for j in range(1,d):
      if i[0][i] in i[j]:
        flag+=1
    if((flag+1)==d and i[0][i] not in d):
      d.append(i[0][i])
  d=sorted(d)
  for i in range(len(d)):
    if i==0:
      print(d[i],end='')
    else:
      print('',d[i],end='')    

d=input().split()
d=list(map(int,d))
k=[]
for i in range(d[0]):
  k.append(list(map(int,input().split())))
repeat(d[0],d[1],k)
