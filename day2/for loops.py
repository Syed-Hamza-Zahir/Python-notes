list_data = [1,2,3,4,5]
embedded_list = [[1,2,3],[4,5,6]]
dict_data = {
    1:{"name":"Bronson", "money":"$0.05"},
    2:{"name":"Masha", "money":"$3.66"},
    3:{"name":"Roscoe", "money":"$1.14"}}


for num in list_data: #"num2 is an empty variable that gos thorugh each index in the list "list_data"
    print(num *2) # needs to be indented
    print("Hello :)")
    print("Testing")

for data in embedded_list:
    print(data)
    print(type(data))
    for num in data:            #nested loop/ nested list
        print(num)

for value in dict_data:
    print(value)
for item in dict_data.values():
    print(item)

for items in dict_data.values():
    print(items["money"])

for num in list_data:
    if num == 3:
        print("I found three.")
    elif num > 3:
            print("I've gone too far.")
    else:
        print("I found three.")
