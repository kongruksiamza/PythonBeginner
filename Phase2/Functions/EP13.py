# Factorial
def factorial(number):
    if number==1:
        return number
    else :
        return number * factorial(number-1)




x=factorial(8)
print(x)

"""
3!

3
3 x factorial(2)
3 x 2 x 1 = 6


"""

