#reptation of block of codes avoid repetition of code
def add (x,y,z):
    x=x+y+z
    # return x
    print(x)
    # return x


p=int(input("Enter 1st value"))
q=int(input("Enter 2nd value"))
r=int(input("Enter 3rd value"))

# x=add(p,q,r)
x=add(y=r,x=p,z=q)
print(x)