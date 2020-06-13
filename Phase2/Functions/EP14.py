# Fibonacci number

# 0, 1, 

# f0 = ? , f1 = ?

def fibonacci(number):
    if number<=1:
        return number
    else :
        #เลขลำดับถัดไป
        return fibonacci(number-1) + fibonacci(number-2)

for i in range(10): # 0 - 4 
    print(fibonacci(i)) # 0, 1, 1, 2 , 3


"""
i = 0 
i = 1
i = 2
i = 3
i = 4


0 , 1 , 1 , 2 , 3
"""