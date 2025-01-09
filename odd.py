n=int(input("Enter any number"))
i=1
while i<=n:
    if n%2!=0:
        if i%2!=0:
            if i<=(n-2):
                print(i,end=',')
            else:
                print(i)
                
    else:
        print(i)
                 
    i=i+1
            