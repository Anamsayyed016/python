#set()-----collection of data

# s1={1,2,3,3,4,9,11,17}
# s2={4,5,17,89}
# s3={"a","b",1,2,3,88}

# r=s1.union(s2,s3)
# r=s1|s2|s3
# print(r)
# r=s1.intersection(s2,s3)
# r=s1&s2&s3
# print(r)

#set difference 
# r=s2.difference(s1)
# print(r)


#update
# s1={1,2,3,3,4,9,11,17}
# s2={4,5,17,89,54,21}
# s1.update(s2)
# print(s1)
# r=s1.union(s2)
# print(s1)
#union
#update

#add
# s1={1,2,3,3,4,9,11,17}
# s1.add((2,3,9))
# s1.update((2,90,99))
# print(s1)

age=(input("enter age =  "))
if age>=18:
    print("eligible")
else:
    print("not eligible")