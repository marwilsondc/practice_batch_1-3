#initialize number list and even list
number_list = list()
even_list = list()

#create while loop to ask user to input 10 numbers
while len(number_list) < 10:
    user_input = int(input("input a number = "))

    #add inputs to number list
    number_list.append(user_input)

    #evaluate even numbers and add to even list
    if user_input % 2 == 0:
        even_list.append(user_input)

#print results by counting even numbers through len()
print(even_list)
print(len(even_list))