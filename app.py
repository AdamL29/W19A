def divide_number(x):
        if ((x%5 == 0) and (x%3 == 0)):
            print("FizzBuzz")
        elif (x%5 == 0):
            print("Buzz")
        elif (x%3 == 0):
            print("Fizz")
        else:
            print("Try Again")

x = 15
# 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 25, 28, 30, 35
divide_number(x)