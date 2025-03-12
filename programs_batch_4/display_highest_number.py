#initialize valid_flag, current_highest_number
valid_flag = True
current_highest_number = 0

#create while loop to continue asking user for inputs
while valid_flag:
    user_input = input("input a number = ")

    #evaluate whether user_input is invalid (if statement + break) and set valid_flag to false if true
    if user_input.isalpha() or user_input.isspace():
        valid_flag = False
        break

    #explicitly convert user_input to integer
    int(user_input)

    #evaluate whether user_input is higher than current_highest_number
    if user_input > current_highest_number:
        current_highest_number = user_input

    #print current_highest_number
    print(current_highest_number)