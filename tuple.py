# fruit = ("apple",20,100)
# fruit = ("apple",30,100) + ("banana",3533)
# print(fruit)
# print(type(fruit))

#fruit[2]=20 #tuple immutable

# print(id(fruit))
# print(id(fruit[0]),id(fruit[1]),id(fruit[2]))


# number = (12,99) + (78,90)  #create 5 tuple
# number = number + (89,90)
# print(number) #(12,99,78,90,89,90)

# lis = [["ajay", "aman"],(45,67)]
# print(type(lis[1]))


# lis[1][0]=99 #error(tuple)
# lis.pop()
# print(lis)
t = (34,55,[9,5,888])
print(t)
t[2][1]=4444
print(t)


lis = [["ajay", "aman"],(45,[65,44])]


lis[1][1][1]=45454
print(lis)

print(type(lis[1]))
lis[1][1].append(88)
print(lis)

#len(),max(),min(),sum(),index(),count()
#sorted--->return sorted list

# t = (5,25,2,5,)

# a=sorted(t)
# print(a)
t = (23 ,)
print(type(t))

t1 = ("absjd",)
print(type(t1))

t2 = 1,2,3,4,5
print(type(t2))  #function

#empty tuple.

# t=()

# t1 = tuple()
# print(t,t1)

record = ("ajay singh",101,23,5556463102)

record =list(record)
record[3]= 541582662525

print(record)

record = tuple(record)
print(record)


a=9
b=6
a,b=100,700
print(a,b)
