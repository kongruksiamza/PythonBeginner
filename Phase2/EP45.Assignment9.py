#การค้นหาและนับจำนวนตัวอักษรในสมาชิก

message=["aa","aab","cba","bba","aba","cca","aaa","aabaac"]
result=[]

for item in message:
    result.append(item.count("a"))
print(result)