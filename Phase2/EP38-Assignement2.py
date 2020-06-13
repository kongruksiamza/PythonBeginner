# Assignment หาค่ามากสุด / ต่ำสุด / ผลรวม ตัวเลข
number=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    number.append(x)

print(number)
print("ค่าที่น้อยที่สุด คือ ",min(number))
print("ค่าที่มากที่สุด คือ ",max(number))
print("ผลรวม คือ ",sum(number))