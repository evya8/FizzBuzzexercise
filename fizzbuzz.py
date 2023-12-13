from icecream import ic



for num in range(1, 101):
    if num % 15 == 0:
        ic ("FizzBuzz")
    elif num % 5 == 0:
        ic ("Buzz")
    elif num % 3 == 0:
        ic ("Fizz")
    else:
        ic (num)


x = 54
y = 12
ic(x, y, x + y)

