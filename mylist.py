#create an empty list
my_list = []

#append values
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#insert value
my_list.insert(1, 15)
print(my_list)

#extend list
my_list.extend([50, 60, 70])
print(my_list)

#remove last element
my_list.pop(7)
print(my_list)

#sort in ascending order
my_list.sort()
print(my_list)

#find and print index of value 30
print(my_list.index(30))