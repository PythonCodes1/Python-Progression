# Based on the user's input

print("Give me any 2 numbers! I'll find how many y is in x percent!")
x = input("Enter the first number: ");
y = input("Enter the second nubmer: ")

def percentage(x, y):
  return (float(x) * float(y)) / 100.0

print("{0}% of {1} is equal to {2}".format(x, y, percentage(x, y)));
