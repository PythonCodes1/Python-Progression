# Based on the user's input

print("Give me any 2 numbers! I'll find the percentage of them!")
x = input("Enter the first number: ");
y = input("Enter the second nubmer: ")

def percentage(x, y):
  return 100 * float(x)/float(y)

print("The percentage of {0} and {1} is {2}".format(x, y, percentage(x, y)));
