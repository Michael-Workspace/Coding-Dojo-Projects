#1. Countdown - Create a function that accepts a number as an input. Return a new list that count down by one, from the number(as the 0th element) down to 0 (as the last element).
print("Answer 1:")
def countdown(high):
    output = []
    for i in range(high,-1,-1):
        output.append(i)
    return output

print(countdown(5)) #input value

#2. Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
print("Answer 2:")
def print_and_return(x):
    print(x[0])
    return x[1]

print(print_and_return([1,2])) #input value

#3. First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
print("Answer 3:")
def first_plus_length(x):
    return x[0]+len(x)

print(first_plus_length([1,2,3,4,5])) #input value

#4. Value Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False.
print("Answer 4:")
def values_greater_than_second(x):
    output = []
    if len(x) <2:
        return False
    for i in range(0,len(x)):
        if x[i]>x[1]:
            output.append(x[i])
    print(len(output))
    return output

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5. This Length, that Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
print("Answer 5:")
def length_and_value(a,b):
    output=[]
    for i in range(0,a):
        output.append(b)
    return output

print(length_and_value(4,7))
print(length_and_value(6,2))
