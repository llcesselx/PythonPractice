#!/usr/bin/env python3

user_data = "0"
numbers = 0
number_list= []
numbers_mean = 0

while user_data != "":
    try:
        user_data = input("Enter a number: ")
        numbers += float(user_data)
        number_list.append(user_data)
        print(numbers)
        print(number_list)
    except ValueError:
        break

if user_data == "":
    numbers_mean = numbers / (len(number_list))
    pass

print("Avg = ", numbers_mean)
