sum = 0 
while True:
    number=int(input("ป้อนตัวเลขของคุณ :"))
    sum+=number # บวกเลขที่ป้อนแต่ละรอบ
    if sum>=100:
        break
    print("ผลรวม = ", sum)
