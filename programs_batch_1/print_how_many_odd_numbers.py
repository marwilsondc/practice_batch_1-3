#initialize odd list and number list
number_list = list()
odd_list = list()

#create while loop to ask user to input 10 numbers
while len(number_list) < 10:
    user_input = int(input("input a number = "))

    #add input to number list
    number_list.append(user_input)

    #evaluate input and append odd numbers to odd list
    if user_input % 2 != 0:
        odd_list.append(user_input)

#return odd list and length of odd list
print(odd_list)
print(len(odd_list))