#initialize number_list and display_list
number_list = list()
display_list = list()

#create while loop to ask user for 10 inputs
while len(number_list) < 10:
    user_input = int(input("input a number = "))

    #append user_input to number_list 
    number_list.append(user_input)

    #evaluate inputs with duplicates (if statement) and append user_input to display_list if true
    if number_list.count(user_input) > 1:
        
        #evaluate once more if the input is duplicated in display_list, break if duplicated, continue if not
        if display_list.count(user_input) > 1:
            break

        elif display_list.count(user_input) == 0:
            display_list.append(user_input)

#display display_list
print(display_list)