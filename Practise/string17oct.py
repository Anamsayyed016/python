
#1=sequence(ordered)
#2immutable

# msg="string is a immutable data-type"
# msg[3]="y"
# print(msg[12:21])

msg="apple good for health"

#capitalize()=====return Capitalized string
a=msg.capitalize()
print(a)

#upper()
b=msg.upper()
print(b)

#lower()
c=msg.lower()
print(c)

#isupper()=====return boolean output
a=msg.isupper()
print(a)

a=msg.islower()
print(a)

msg = "5253321"

a=msg.isupper()
print(a)

a=msg.islower()
print(a)

#isdigit
#isalpha

msg="ddjdjdjdjjd"
b=msg.isalpha()
print(b)

msg="522533222"
b=msg.isdigit()
print(b)

#replace(old_value, new_value)
s= "we are here to learn c++, it is a high level lang"
s1=s.replace("c++","python")
s2=s.replace("a","b",1)
s3=s.replace(s,"new")
print(s1)
print(s2)
print(s3)

#split()-->return list
s= "we are here to learn c++, it is a high level lang here"
s1=s.split()
print(s1)

s1=s.split('a')
print(s1)

s2=s.split('here',1)
print(s2)

#join()---> return string
lis = ["apple","banana","pineapple", "orange",'"4524"']
lis2 = ["1","2","3", "4"]
s=" ,".join(lis) +" " + " , ".join(lis2)
print(s)



s="its now or never"
s=s.split()
print(s)
a=s[0][::-1]
b=s[1][::-1]
c=s[2][::-1]
d=s[3][::-1]
s=[a,b,c,d]
print(s)


s=" Apple Banana"
a=s


