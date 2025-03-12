#initialize valid_flag, number_list
valid_flag = True
number_list = list()

#create while loop to keep asking user to input numbers
while valid_flag:
    user_input = input("input a number = ")

    #evaluate whether user_input is invalid (if statement + break) and set valid_flag to false if true
    if user_input.isalpha() or user_input.isspace():
        valid_flag = False

    #explicitly convert user_input to integer and store in convert_input
    convert_input = int(user_input)

    #append convert_input into number_list
    number_list.append(convert_input)

    #print sum of number_list and divide to length of number_list
    print(sum(number_list)/len(number_list))