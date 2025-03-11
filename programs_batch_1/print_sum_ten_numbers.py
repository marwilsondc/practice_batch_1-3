#initialize a list to store 10 number inputs
number_list = list()

#create while loop to append 10 numbers
while len(number_list) < 10:
    number_list.append(int(input("input a number = ")))

#print sum of 10 number list
print(sum(number_list))