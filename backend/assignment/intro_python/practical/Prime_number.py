#get number 
n= int(input("enter number "))
prime=0 
#chech prime numbr
for i in range (1,n+1):
   
    if n%i==0:
        prime=prime+1

    if prime==2: 
        print(n,"that is prime number ")
    else:
        print(n, "prime number" )

