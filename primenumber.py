n=int(input("Enter a positive integer: "))
flag=0

if(n==0 or n==1):
    flag=1

for i in range(2,n//2+1):
    if(n%i==0):
        flag=1
        break

if(flag==0):
    print(n," is prime number")
else:
    print(n," is not prime number.")