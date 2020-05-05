num1 = float(16)
num2 = float(12.5)

answer = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, answer))

"""
Output:
The sum of 16 and 12.5 is 28.5
"""
# There are many other equations you can apply, but this is a simple way to represent easy arithmetic

# You can also create an equation through the user's input
num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

answer = float(num1) + float(num2)

print('The sum of {0} and {1} is {2}'.format(num1, num2, answer))

# In addition, you can create the same exact thing without even using variables
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

"""
Things learned:
format()
input()
Basic Arithmetic
Creating Separate Variables for different purposes
Using % instead of variables
One-liners
"""
