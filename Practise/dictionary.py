#
# d={"one":"monday","two":"tuesday","three":"wednesday"}
# print(d)

# print(d["two"])

# d={"1":"monday","2":"tuesday","3":"wednesday"}
# print(d)
# d["4"]="thursday"
# d["5"]="friday"
# d.update({"6":"saturday"})
# # d.update({"7":"sunday"})
# d1={"7":"sunday"}
# d.update(d1)
# print(d)
# d={1:["ajay",23,"bhopal"],2:["jay",23,"ujjain"]}
# print(d)
# print(d[1])
# print(d[1][2])

# d[2][2]="delhi"
# print(d)



# d1 = {101:{"name":"ajay","age":23,"city":"bhopal"},
#     102:{"name":"jay","age":23,"city":"ujjain"}}

# print(d1)
# print(d1[101])
# print(d1[101]["city"])

# print(d1[102]["age"])


d={1:"mon", 2:"tue",3:"wed"}

#key()
# keys=d.keys()
# print(keys,type(keys))

#values()
# values=d.values()
# print(values,type(values))

#items()
# items=d.items()
# print(items,type(items))

# sorted_keys=sorted(d.keys())
# print(keys,type(keys))

#zip
# key = ["Ajay","Vikas","Arun","Sonam","Naman"]
# value = [23,24,45,27,95]

# result = dict(zip(key,value))
# print(result)

# result = tuple(zip(key,value))
# print(result)

# result = list(zip(key,value))
# print(result)

#get(key)----> Return value

data = {"Ajay":23,"Vikas":14,"Arun":56}
# a=data["Ajay"]
a=data.get("Aman")
print(a)

#setdefault()


# data = {'1':2390,'2':4524,'3':7486}
# value = data.setdefault('11',3333)

# print(data,value)


#pop()
#popitem()
#clear()

# value=data.pop('2')
# print(data,value)

# value=data.popitem()
# print(data,value)

# data = {'1':2382,'2':4524,'3':4514,
#       '4':{'11':5354 ,'22':52545,'44':4554}}


# data['4'].popitem()
# print(data)

# data.popitem()

#set




