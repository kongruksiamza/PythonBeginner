# แม่สูตรคูณ

start=int(input("ป้อนแม่สูตรคูณเริ่มต้น = ")) # 1
stop=int(input("ป้อนแม่สูตรคูณสุดท้าย = ")) # 4

for x in range(start,stop+1):
    print("แม่ = ",x)
    for y in range(1,13):
        print(x,'x',y ," = ",(x*y))
