n=int(input("Enter any number"))
i=1
sum=0
while i<=n:
    if n%2!=0:
        sum=sum+1
        if i<n:
                print(2*i,end='+')             
    else:
        print(2*i)              
    i=i+1

            