#initialize valid_flag and number_list
valid_flag = True
number_list = list()

#create a while loop to continue asking user for inputs
while valid_flag:
    user_input = (input("input a number = "))

    #within while loop, append user_input to number_list
    number_list.append(user_input)

    #evaluate user_input if it's invalid (if statement) and set valid_flag to false if true
    if user_input.isalpha() or user_input.isspace():
        valid_flag = False
    
    #evaluate user_input if it's unique (if statement) and return "unique" if true
    elif number_list.count(user_input) == 1:
        print("unique")

    #evaluate user_input if it's a duplicate (if statement) and return "duplicate" if true
    elif number_list.count(user_input) > 1:
        print("duplicate")