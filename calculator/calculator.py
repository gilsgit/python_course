from art import logo


def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1/n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}



print(logo)

def calculate():
    start_over = False

    n1 = int(input("Enter first number: "))

    while not start_over:

        print("""
        + = addition
        - = subtraction
        * = multiply
        / = divide 
        """)
        math_operator = input("Enter a math operator from above:")
        n2 = int(input("Enter second number: "))

        answer = (operations[math_operator](n1, n2))
        print(f"The answer is : {answer}")

        again = input("Type 'y' if you want to start over with the answer as the first number or 'n' to stop:")

        if again == 'y':
            n1 = answer
            print(f"First number = {answer}")
        else:
            start_over = True
            calculate()

calculate()

