#Design a program that asks the user to enter a series of numbers. The program should store the numbers in a list then display the following data:
#The lowest number in the list
#The highest number in the list

def get_lowest_list_value(num_list_l):
    lowest_num = num_list_l[0]
    for i in range(len(num_list_l)):
        if num_list_l[i] < lowest_num:
            lowest_num = num_list_l[i]
    return lowest_num

def get_highest_list_value(num_list_h):
    highest_num = num_list_h[0]
    index = 0
    while index < len(num_list_h):
        if num_list_h[index] > highest_num:
            highest_num = num_list_h[index]
        index += 1
    return highest_num
    