'''
my_dict = {}
# or
my_dict = dict()
'''
'''
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
'''
'''
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 25
'''
'''
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict['age'] = 30
print(my_dict['age'])  # Output: 30
'''

'''
my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
print(my_dict)  # Output: {'name': 'John', 'age': 25, 'city': 'New York'}
'''

'''
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['age']
print(my_dict)  # Output: {'name': 'John', 'city': 'New York'}
'''


'''
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Iterating over keys
for key in my_dict:
    print(key)  # Output: name, age, city

# Iterating over values
for value in my_dict.values():
    print(value)  #
'''

'''
# Basic Dictionary Operations
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}

# Accessing Values
print(my_dict['name'])  # Output: John

# Modifying Values
my_dict['age'] = 30
print(my_dict['age'])  # Output: 30

# Adding Key-Value Pairs
my_dict['occupation'] = 'Engineer'
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'city': 'New York', 'occupation': 'Engineer'}

# Removing Key-Value Pairs
del my_dict['city']
print(my_dict)  # Output: {'name': 'John', 'age': 30, 'occupation': 'Engineer'}

# Dictionary Methods and Operations
print(my_dict.keys())    # Output: ['name', 'age', 'occupation']
print(my_dict.values())  # Output: ['John', 30, 'Engineer']
print(my_dict.items())   # Output: [('name', 'John'), ('age', 30), ('occupation', 'Engineer')]

print(my_dict.get('name'))  # Output: John
print(my_dict.get('salary', 0))  # Output: 0 (default value if key doesn't exist)

print(my_dict.pop('age'))  # Output: 30 (removes and returns the value)

# Iterating Over a Dictionary
for key, value in my_dict.items():
    print(key, value)
# Output:
# name John
# occupation Engineer

# Dictionary Comprehension
numbers = {'one': 1, 'two': 2, 'three': 3}
squared_numbers = {key: value ** 2 for key, value in numbers.items()}
print(squared_numbers)  # Output: {'one': 1, 'two': 4, 'three': 9}

# Nested Dictionaries
employees = {
    'John': {'age': 30, 'position': 'Manager'},
    'Emma': {'age': 28, 'position': 'Engineer'}
}

print(employees['John']['position'])  # Output: Manager

# Merging Dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}
'''