#initialize a number list and display list
number_list = list()
display_list = list()

#create a while loop to ask user to input 10 numbers
while len(number_list) < 10:
    user_input = int(input("input a number = "))

    #append user inputs to number list and display list
    number_list.append(user_input)
    display_list.append(user_input)

    #evaluate whether user input is already in number list (if statement)
    if number_list.count(user_input) > 1:

        #pop duplicated inputs from display list
        while user_input in display_list:
            display_list.remove(user_input)

#display results from display list
print(display_list)