#initialize valid_flag and number_list
valid_flag = True
number_list = list()

#create while loop that continuously asks user for integer inputs
while valid_flag: 
    user_input = input("input a number = ")

    #evaluate whether user_input is invalid (if statement) and set valid_flag to false if true
    if user_input.isalpha() or user_input.isspace():
        valid_flag = False
        break

    #append user_input to number_list and use sort()
    number_list.append(int(user_input))
    number_list.sort()

    #display lowest number with list indexing
    print(number_list[0])
    
