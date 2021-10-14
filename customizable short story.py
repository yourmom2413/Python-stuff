Character_name = ""
Character_age = ""
Character_pronoun = ""
Character_pronoun2 = ""

def function2():
    global Character_age
    global Character_name
    global Character_pronoun
    global Character_pronoun2
    Character_name = input ("what is the characters name: ")
    if Character_name == "jack" or Character_name == "Jack":
        global Character_age
        global Character_pronoun
        global Character_pronoun2
        Character_age = "14"
        Character_pronoun = "boy"
        Character_pronoun2 = "he"
        print5()
   
    Character_age = input ("What is the characters age: ")
    Character_pronoun = input ("Are they a girl or boy: ").lower()

    if Character_pronoun == "boy":
        Character_pronoun2 = "he"
        print5()
    elif Character_pronoun == "girl":
        Character_pronoun2 = "she"
        print5()

def print5():
    print ("\nThere once was " + Character_pronoun + " named " + Character_name + ", ")
    print (Character_pronoun2 + " was " + Character_age + " years old. ")
    print (Character_pronoun2 + " really liked the name " + Character_name + ", ")
    print ("but didn't like being " + Character_age + ".")

    input("\npress enter to quit")

function2()
#hi i am funny and pooping #flowerpower