while True:
    print("1.add\ 2.sub\ 3.multi\ 4.div\ 5.off")
    n=int(input("Enter your choice:"))
    x=[1,2,3,4]
    if n in x:
        x=int(input("Enter 1st value"))
        y=int(input("Enter 2nd value"))
        if n==1:
            print("add",x+y)
        elif n==2:
            print("mul",x-y)
        elif n==3:
            print("sub",x*y)
        elif n==4:
            print("div",x/y)
    elif n>=5:
        break
    else:
        print("invalid choice")
