#The lowest number in the list
#The highest number in the list

import lists

def menu():
    print("------MENU------\n1-Show the list low /high values\n2-Exit")

def get_num_list():
    list = []
    while True:  
        if len(list) > 2:
            answer = input("Do you want to enter another value? y/n ").upper()
            if answer == "Y":
                num = int(input("please enter a integer value: "))
                list.append(num)
            if answer == "N":
                break
        else:
            num = int(input("please enter a integer value: "))
            list.append(num)

    return list
    
def run_menu():
    option = 0
    while option != 2:
        menu()
        option = int(input("please enter your selection: "))
        list = []
        
        if option == 1:
            list = get_num_list()
            lowest_value = lists.get_lowest_list_value(list)
            highest_value = lists.get_highest_list_value(list)
            print(f"for list{list}, the lowest value is {lowest_value}, the highest value is {highest_value}")
            
        elif option == 2:
            exit()

        else:
            exit()

run_menu()