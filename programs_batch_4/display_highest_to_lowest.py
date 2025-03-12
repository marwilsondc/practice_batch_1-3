#initialize valid_flag, number_list
valid_flag = True
number_list = list()

#create while loop to keep asking user for inputs
while valid_flag:
    user_input = input("input a number = ")

    #evaluate whether user_input is invalid (if statement + break) and set valid_flag to false if true
    if user_input.isalpha() or user_input.isspace():
        valid_flag = False
        break

    #explicitly convert user_input into integer and store it in convert_input
    convert_input = int(user_input)

    #append user_input and use sort(reverse=True) to arrange list in descending order
    number_list.append(convert_input)
    number_list.sort(reverse=True)

    #display number_list until program ends 
    print(number_list)