# หาจำนวนตัวอักษรพิมพ์เล็ก/พิมพ์ใหญ่

def checkString(message):
    result={"UPPER":0,"LOWER":0}
    for c in message:
        if c.isupper():
            result["UPPER"]+=1
        elif c.islower():
            result["LOWER"]+=1
        else:
            pass
    return result

message=input("input your message :")
x=checkString(message)
print(x)