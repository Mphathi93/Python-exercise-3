# Question 1: Basic Function Definition and Calling

# TODO: Define a function called 'greet' that prints "Hello, World!"
def greet():
    print('Hello World!')
# TODO: Call the 'greet' function
greet()

# ------------------------------------------------------------------------------------
# Question 2: Function with Parameters

# TODO: Define a function called 'personalized_greeting' that takes a name as a parameter and prints a personalized greeting
name = input("name: ")
def pgreeting():
    print(f'Hello {name}')

# TODO: Call the 'personalized_greeting' function with your name
pgreeting()

#------------------------------------------------------------------------------------
# Question 3: Function with Return Value

# TODO: Define a function called 'square' that takes a number as a parameter and returns its square
num = 5
def square(num):
    result = num**2
    print(result)
# TODO: Call the 'square' function with the number 5 and print the result
square(num)

#------------------------------------------------------------------------------------
# Question 4: Function with Multiple Parameters and Return Value

# TODO: Define a function called 'rectangle_area' that takes length and width as parameters and returns the area of the rectangle
length = 4 
width = 5
def rectangle_area(length, width):
    result = length*width
    return result
    
# TODO: Call the 'rectangle_area' function with length 4 and width 5, and print the result
print(f'The rectangle area is {rectangle_area(length, width)}')
#------------------------------------------------------------------------------------
# Question 5: Using a Function as an Argument
number = 7
# TODO: Define a function called 'apply_operation' that takes a function and a number as parameters, and returns the result of applying the function to the number
def apply_operation(function, number):
    return function(number)
# TODO: Define a function called 'double' that takes a number as a parameter and returns its double
def double(number):
    return number*2 
# TODO: Use the 'apply_operation' function with the 'double' function and the number 7, and print the result
result2 = apply_operation(double, number)
print(result2)
# TODO: Use the 'apply_operation' function with the 'square' function (defined in Question 3) and the number 3, and print the result
results = apply_operation(square, 3)
