def divide_number(num):
    for x in range(num):
        if ((x%5 == 0) and (x%3 == 0)):
            print("FizzBuzz")
            continue
        elif (x%5 == 0):
            print("Buzz")
            continue
        elif (x%3 == 0):
            print("Fizz")
            continue
        else:
            print("Try Again")

divide_number(16)