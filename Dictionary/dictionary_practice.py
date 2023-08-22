my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.clear()
print(my_dict.keys())
print(my_dict.values())
print(my_dict['age'])
print(my_dict['name'])
my_dict['country'] = "usa"
my_dict['age'] = 30
del my_dict['age']
print(my_dict)
for i in my_dict:
    print(my_dict[i])