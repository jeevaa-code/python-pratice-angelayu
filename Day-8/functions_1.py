#function:
print("hello")
num_char = len("Hello")
print(num_char)
#now we are going to built a function:
#after giving paraenthesis It will become function..
#defining the function
#function is bundling all the instructions....
#all code inside the function is indntended
def my_function():
    print("hello")
    print("bye")

# call the function:
my_function()

#functions with inputs
def greet(name = "Angela"):
    print(f"hello {name}")
    print(f"{name} coders")
    print(f"{name} hackers")
    #do_this
    #then do this
    #finally do this

greet("jeevaa")

#name = parameter(name of the value that is passed in)
#Angela = arguments (actual value)

#functions with more than 1 inputs:
def greet(name,location):
    print(f"hello {name}")
    print(f"I am in {location}")

#positional argument
#greet("jeevaa","jolarpet")

#keyword_argument
greet(location="jolarpet",name="jeevaa")