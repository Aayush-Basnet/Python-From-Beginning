n= int(input("Give the number upto you want sum: "))
s=0

for i in range(0,n):
    if(i%2!=0):
        s=s+i

print(s)