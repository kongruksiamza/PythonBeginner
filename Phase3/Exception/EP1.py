# #Exception
while True:
    try:
        name=input("ป้อนชื่อผู้ใช้โปรแกรม :")
        if name == "ก้อง":
            raise Exception("มีชื่อในระบบแล้วนะครับ")
        
        number1=int(input("ป้อนตัวเลข 1 :"))
        number2=int(input("ป้อนตัวเลข 2 :"))
        if number1 == 0 and number2 == 0:
            break
        if number1<0 or number2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้นะครับ")

        result=number1/number2
        print(result)
    except Exception as e:
        print(e)

#ValueError => ค่าผิดพลาด
#ZeroDivisionError