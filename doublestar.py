def show(**kwards):
    print(kwards)
    for i,j in kwards.items():
        print(i,"=",j)

show(name='anam',age=27) 