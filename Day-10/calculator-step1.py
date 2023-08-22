def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide (n1, n2):
    return n1/n2

calculator_dictonary = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculation1():
    from art import logo
    print(logo)
    n1 = float(input("number1: "))


    for i in calculator_dictonary:
        print(i)

    is_true = True
    while (is_true):
        operation_symbols = input("which operation need to perform :  ")
        n2 = float(input("next_number: "))
        calculation = calculator_dictonary[operation_symbols]
        answer = calculation(n1,n2)
        print(f"{n1} {operation_symbols} {n2} = {answer}")
        solution = input(f"Type y to continue calculating with {answer} or type n to exit ").lower()
        if solution == "y":
            is_true = True
            n1 = answer
        else:
            is_true = False
            calculation1()
            """IT is called recursion"""

calculation1()


