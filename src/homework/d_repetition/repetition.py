#GET_FACTORIAL_and_WHILE_LOOP_YQ

def get_factorial_y(num1):
    TOTAL_X = 1
    for X in range(num1, 0, -1):
        TOTAL_X = TOTAL_X * X
    return TOTAL_X


def sum_odd_numbers_y(num2):
    Y = 1
    TOTAL_Y = 0

    while Y <= num2:
        if Y%2 == 1:
            TOTAL_Y = TOTAL_Y + Y
        Y = Y + 1
    
    return TOTAL_Y



def main_menu():
    print("----MENU----\n1-FACTORIAL\n2-SUM ODD NUMBERS\n3-EXIT")
    
def run_menu():
    OPTION = 0

    while OPTION != 3: 

        main_menu()
        OPTION = int(input("PLEASE ENTER YOUR SELECTION: "))
        run_the_option(OPTION)
         

def run_the_option(OPTION):

    if OPTION == 1:
        NUM1 = int(input("PLEASE ENTER A NUMBER: "))
        if NUM1 > 0 and NUM1 < 10:
            RESULT1 = get_factorial_y(NUM1)
            print("RESULT: ", RESULT1)
        else:
            print("PLEASE ENTER A NUMBER AGAIN")

    elif OPTION == 2:
        NUM2 = int(input("PLEASE ENTER A NUMBER: "))
        if NUM2 > 0 and NUM2 < 100:
            RESULT2 = sum_odd_numbers_y(NUM2)
            print("RESULT: ", RESULT2)
        else:
            print("PLEASE ENTER A NUMBER AGAIN")

    elif OPTION == 3:
        print("DO YOU WANT TO CONTINUE?\n1-yes\n2-no")
        OPTION2 = int(input("PLEASE ENTER YOUR SELECTION: "))

        if OPTION2 == 1:
            run_menu()

        elif OPTION2 == 2:
            ask_for_exit()
            
        else:
            print("INVALID OPTION")
            exit()

    else:
        print("INVALID OPTION")


def ask_for_exit():
    CHOICE = input("DO YOU WANT TO EXIT?\nPLEASE ENTER Y OR N")

    if CHOICE == "Y" or CHOICE == "y":
        print("THANK YOU!")
        exit()
    
    else:
        print("INVALID")
        exit()