#initialize number_list and display_list
number_list = list()
display_list = list()

#create while loop that asks user for 10 integer inputs
while len(number_list) < 10:
    user_input = int(input("input a number = "))

    #append user inputs to number_list and display_list
    number_list.append(user_input)
    display_list.append(user_input)

    #evaluate duplicated inputs in number_list (if statement)
    if number_list.count(user_input) > 1:

        #remove duplicated inputs in display_list until its count turns to 1
        while display_list.count(user_input) > 1:
            display_list.remove(user_input)

#display results
print(display_list)