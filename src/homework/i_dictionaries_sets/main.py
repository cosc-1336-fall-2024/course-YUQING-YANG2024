#get p-distance for every pair of strings in a collection

import dictionary
"""
def menu():
    print("----MENU----\n1-Get p distance matrix\n2-Exit")

#make the result output to a matrix
def display_result(result):
    for row in result:
        for item in row:
            print(str(item).rjust(3, " "), end = " ")
        print(" ")

#make the input to a list, make the lists into a total list
def get_total_list():
    num = int(input("how many list will enter? "))
    index = 0
    total_list = []

    while(index < num):
        input_list = input("please enter a comma-separated list: ")
        s_list = input_list.split(",")
        s_list = [value.strip() for value in s_list]
        total_list.append(s_list)
        index += 1

    return total_list


def run_menu():
    option = 0
    while option != 2:
        menu()
        option = int(input("please enter your selection: "))
        result = []
        
        if option == 1:
            result0 = get_total_list()
            result = dictionary.get_p_distance_matrix(result0)
            display_result(result)

        elif option == 2:
            exit()

        else:
            exit()

run_menu()
"""

#HW8
def menu():
    print("Inventory Menu\n1-Add or Update Item\n2-Delete Item\n3-Exit")

def run_menu():
    option = 0
    widget_dictionary = {}
    while option != 3:
        menu()
        option = int(input("please enter your selection: "))
        if option == 1 or 2:
            if option == 1:
                key = input("please enter widget name: ")
                value = input("please enter the quantity: ")   
                dictionary.add_inventory(widget_dictionary, key, value)
                print("widgets_dictionary is: ", widget_dictionary)

            if option == 2:
                key = input("please enter the widget name you want to delete: ")
                dictionary.remove_inventory(widget_dictionary, key)
                print("widgets_dictionary is: ", widget_dictionary)
                
        elif option == 3:
            exit()
        else:
            exit()

run_menu()
