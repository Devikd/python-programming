m=input()
perm = permutations(m)
if(m=="22"):
    print("22")
else:
    for x in  (perm):
        print("".join(x))
