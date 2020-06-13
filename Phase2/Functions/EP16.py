# lambda function


def myPower(x):
    # x= ตัวเลข
    # a = เลขชื้กำลัง
    return lambda a : 5**a


y=myPower(5)
result=y(3)

print(result)