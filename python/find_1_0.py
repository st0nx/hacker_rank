ar = (1,1,0,0,1,1,0,0,1,1,1)

num = 1

while num <= len(ar)-1:
    if ar[num] != ar[num-1]:
        print("FIND "+str(num-1))
    if num+1 < len(ar) and ar[num] != ar[num+1]:
        print("FIND "+str(num))
    num+=2
