def calc():
    try:
        Number = input("Type Equation: ")

        print(str(eval(Number)))
        calc()
    except:
        print("Error!")
        calc()

calc()