#initialize valid_flag, number_list, high_duplicate, high_duplicate_count
valid_flag = True
number_list = list()
high_duplicate = 0
high_duplicate_count = 0

#create while loop to keep asking user for inputs
while valid_flag:
    user_input = input("input a number = ")

    #evaluate user_input if invalid (if statement + break) and set valid_flag to false if true
    if user_input.isalpha() or user_input.isspace():
        valid_flag = False
        break

    #explicitly convert user_input to integer
    convert_input = int(user_input)

    #append user_input to number_list``
    number_list.append(convert_input)

    #evaluate whether number_list.count(user_input) is higher than high_duplicate_count
    if number_list.count(convert_input) > high_duplicate_count:

        #if true, overwrite the value of high_duplicate_count and high_duplicate
        high_duplicate_count = number_list.count(convert_input)
        high_duplicate = convert_input

    #print(high_duplicate)
    print(high_duplicate)
   
