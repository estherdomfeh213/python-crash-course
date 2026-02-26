# Use the third argument of the range() function to make
# a list of the odd numbers from 1 to 20. Use a for loop to print each number

#!range(start, stop, step)
#! note to self: start: 1 , stop: 21, step:2(skips every even number)
odd_numbers = list(range(1, 21,2))

for number in odd_numbers:
    print(number)