def get_question():
    global question
    question = input("Enter your question (Enter 'exit' to quit) : ")

    if question == "exit" or question == "Exit" or question == "EXIT":
        print()
        print("_________________________________________________________________________________")
        print("                                    GoodBye                                      ")
        print("¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯¯")

        return 0
    
    else:
        values = question.split(" ")

        if len(values) < 3:
            print("Invalid!!")
            print()
            print()

            get_question()

        else:
            calculate_answer(values)
    
def calculate_answer(values):
    value_1 = int(values[0])
    value_2 = int(values[2])
    operator = values[1]

    try:
        if operator == "+":
            answer = add(value_1,value_2)

        elif operator == "-":
            answer = minus(value_1,value_2)

        elif operator == "*":
            answer = multiply(value_1,value_2)

        elif operator == "/":
            answer = divide(value_1,value_2)

        elif operator == "%":
            answer = modulus(value_1,value_2)

        print(f"{question} = {answer}")
    
    except:
        print("Error!!")
        print()
        print()

    get_question()
    
def add(x,y):
    return x + y

def minus(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def modulus(x,y):
    return x % y

print("                               Python Calculator                                ")
print("---------------------------------------------------------------------------------")
get_question()