#append ---->lis.append(element)
# lis = [23,45,6,7,88]

# print(lis)
# lis.append(10)
# print(lis)

# lis.append(["mango,banana"])
# print(lis)
# print(lis[6])
# print(lis[6][0])

# lis = [['mango', 'banana'], ['200/kg','50/dozen']]
# print(lis)
# lis[0].append("apple")

# lis[1].append("50/kg")
# print(lis)

   #extend-->list.extend
# lis=['mango', 'banana','apple']
# print(lis)
# lis.extend(["pineaple", "orange"])
# print(lis)
# lis.append(["mango,banana"])
# print(lis)

  #insert(index,element)

# lis.insert(3,"table")
# print(lis)


# lis[5]="chair"
# print(lis)

#len()
#max()
#min()
#sum()

# list = [23,4,-5,6,77]

# m = max(list) 
# print(m)

# m = min(lis)
# print(m)

# m = len(list)
# print(m)

# nums = [2,43,45,56,7,45,9,-33,44,45,6,45,5]
# fruit = ["apple" , "banana", "orange"]
#max
# a=min(fruit)
# print(a)
# a=sum(nums)
# print(a)
# a=max(fruit)
# print(a)

#nums ,  imdex(element,start,end)

# a=nums.index(45)
# print(a)
# b=nums.index(45,a+1)
# print(b)
# c=nums.index(45,b+1)
# print(c)
# d=nums.index(45,c+1)
# print(d)
# -------------------------------------------practise------------------------------------------------------------------
# a=nums.count(2)
# print(a)

  #sorting function--sort()---- none return
  #inplace function
  #no need of extra list(object)

# nums.sort()
# print(nums) #increasing

# nums.sort(reverse=True) #decresing
# 

#reverse function

# lis1= ['ajay', 'sourabh','aditya']
# print(lis1)
# lis1.reverse()
# print(lis1)

#pop()
#remove()
#clear()
#del()

#pop(index)
#deleted index element ----> return deleted element
# lis1= ['ajay', 'sourabh','aditya','mandeep']
# print(lis1)

# deleted_value=lis1.pop(3)#if did not give a index num then last element will be deleted
# print(lis1)
# print(deleted_value)

# a=lis1.append("xyz")
# print(a)

  #remove--> its remove  1 element  at a time
# lis1= ['ajay', 'sourabh','aditya','aditya','aditya','mandeep']
# print(lis1)
# c = lis1.count('aditya')
# print(c)

# eleted_value=lis1.remove('aditya')
# eleted_value=lis1.remove('aditya')

# print(lis1)
# print(deleted_value)

#clear
# lis1= ['ajay', 'sourabh','aditya','mandeep']
# lis1.clear()
# print(lis1)

#delete(del)  ----- statment
# lis1= ['ajay', 'sourabh','aditya','mandeep']
# print(lis1)

# del lis1
# print(lis1)

        #listslicing
        #list[staer:end:jump]
        #jump   default  1
        #end     exculded(just before end)
  #    0   1  2    3        4         5  6   7     8       9  10  11 12  13
# lis2= [12 ,5 ,8 ,'ajay' ,'sourabh' , 87 ,9 ,23 ,'aditya' ,85 ,41 ,5 ,2 ,'mandeep']
  #   -14 -13 -12 -11     -10        9   8   7     6      5    4  3  2    1

# a=lis2[3 : 8 : 1]
# print(a)

# b = lis2[3 : 8 : 1]
# print(b)


#       0   1    2  3    4        5      6  7  8
lis3 = [54, 5 , 3 , 8 ,"ajay", 'sourabh',59,20,45,]
#      -9  -8  -7  -6   -5       -4     -3  -2  -1

a = lis3 [1 : 5  :  7]
print(a)

