n=int(input("Enter an integer: "))
reversed=0
remainder=0
original=n

while(n!=0):
    remainder=n%10
    reversed=reversed*10+remainder
    n//=10

if(original==reversed):
    print(original," is a palindrome")
else:
    print(original," is not palindrome")