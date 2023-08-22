def my_function():
    result = 3*2
    return result

output = my_function()
print(output)

def format_name(f_name,l_name):
    """Take a first and lastname and make a title in it..."""
    if f_name == "" and l_name == "":
        return
    formated_f = (f_name.title())
    formatted_l = (l_name.title())
    return f"{formated_f} {formatted_l}" #It will be the end of the function.
print(format_name(input("What is your first name \n"),input("What is your last name \n")))

"""DocString - It is a little bit of documentation in coding coding along in our function and documentation..."""
