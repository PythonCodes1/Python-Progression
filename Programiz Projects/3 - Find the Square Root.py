# Finding the square root of 8
num = 8
sqrt = num ** 0.5

print("The square root of {:0.3f} is {:0.3f}".format(num, sqrt))

# Finding the square root of complex numbers using the cmath module
import cmath
num = 1+2j
sqrt = cmath.sqrt(num)

print('The square root of {0} is {1:0.3f}+{2:0.3f}j'.format(num, sqrt.real, sqrt.imag))
