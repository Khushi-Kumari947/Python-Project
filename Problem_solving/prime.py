n=int(input("Enter a number:"))
flag=0
if(n==1):
    print("Not a prime nummber")
for i in range(2,n):
    if(n%i==0):
        flag=1
        break
if(flag==1):
    print("Not a prime number")
else:
    print("Prime number")