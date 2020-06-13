# *agrs

def add(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

add(10,5)
add(10,5,6)
