# if ซ้อน if
age=int(input("ป้อนอายุของคุณ : "))

if age<=15:
    if age==15:
        print("ม.3")
    elif age==14:
        print("ม.2")
    elif age==13:
        print("ม.1")
    else :
        print("ประถมศึกษา")
else :
    print("ม.ปลาย")

print("จบโปรแกรม")