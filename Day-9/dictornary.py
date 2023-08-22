#{key: value}
#{"bug: An error in a program that prevents the program from running as expected
# function : A piece of code that you easily call over and over again
# loop : The action of doing something over and over again}

programming_dictonary = {
  "bug":"An error in a program that prevents the program from running as expected",
  "function":"A piece of code that you easily call over and over again",
}

print(programming_dictonary["bug"])

programming_dictonary["loop"] = "The action of doing something over and over again"
print(programming_dictonary)

#we can create empty dictonary

empty_dictonary = {}

#programming_dictonary = {}

#print(programming_dictonary)

#edit an item in dictornary

programming_dictonary["bug"] = "A moth in computer"

print(programming_dictonary)


#loop thorough in dictonary

for i in programming_dictonary:
  print(i)
  print(programming_dictonary[i])
