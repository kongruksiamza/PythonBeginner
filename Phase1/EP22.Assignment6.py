weight=int(input("ป้อนน้ำหนักของคุณ (kg):"))
high=int(input("ป้อนส่วนสูงของคุณ (cm) :"))/100
bmi = weight/(high**2)

if bmi>=0 and bmi<18.0:
    result="ผอม"
elif bmi>=18.5 and bmi<=22.9:
    result="สมส่วน"
elif bmi>=23.0 and bmi<=24.9:
    result="น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.9:
    result="โรคอ้วน ระดับที่ 1"
elif bmi>30:
    result="โรคอ้วนระดับอันตราย"
else :
    result="ไม่ทราบค่าที่ชัดเจน"

print("ค่า bmi = ", bmi ,"ทำนายว่า =",result)