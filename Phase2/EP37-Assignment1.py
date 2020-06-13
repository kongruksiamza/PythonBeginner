# Assignment รับและเรียงลำดับข้อมูลตัวเลข
number=[]
while True:
    x=int(input("ป้อนตัวเลขของคุณ :"))
    if x<0:
        break
    number.append(x)

print("ก่อนเรียง=>",number)
number.sort()
print("น้อยไปมาก=>",number)
number.reverse()
print("มากไปน้อย=>",number)
print("จบโปรแกรม")