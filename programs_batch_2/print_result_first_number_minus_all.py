#initialize number list
number_list = list()

#create while loop to ask user to input 10 numbers
while len(number_list) < 10:
    number_list.append(int(input("input a number = ")))

#print result by indexing the first number and subtracting the sum of the rest
print(number_list[0] - sum(number_list[1:10]))