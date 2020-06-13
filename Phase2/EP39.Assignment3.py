# Assignment หากลุ่มเลขคู่ / เลขคี่
number=[]
odd=[] #เลขคี่
even=[] #เลขคู่
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    if x%2 == 0:
        even.append(x)
    else :
        odd.append(x)
    number.append(x)

print("ตัวเลขทั้งหมด =>" ,number)
print("เลขคู่ => ",even)
print("เลขคี่ => ",odd)