#ask user to input 2 numbers
first_number = int(input("input first number = "))
second_number = int(input("input second number = "))

#integrate the 2 inputs to range(), add 1 to first number
number_range = range(first_number + 1, second_number)

#create a for loop to iterate through range()
for i in number_range:
    print(i)
