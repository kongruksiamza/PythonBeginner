# Module Date / Time
import datetime

result=datetime.datetime.now() # ดึงวัน/เวลาปัจจุบันมาใช้งาน
# print(result.year) # เอาปีมาแสดง
# print(result.month) # เอาเดือนมาแสดง

newdate=datetime.datetime(2020,6,20,15) # yyyy,m,d
# print(newdate)

#รูปแบบแสดงผล
print("เริ่มต้น = ",result)
print(result.strftime("%x")) # m/d/y สั้น
print(result.strftime("%X")) #เวลา time
print(result.strftime("%c")) 

#เวลา
print(result.strftime("%H:%M:%S %p"))

#1 - 366
print(result.strftime("%j"))

# date
print(result.strftime("%a")) # แบบสั้น
print(result.strftime("%A")) # แบบเต็ม
print(result.strftime("%w")) # 0 = sunday
print(result.strftime("%d")) # วันที่
print(result.strftime("%b")) #เดือนแบบสั้น
print(result.strftime("%B")) #เดือนแบบชื่อเต็ม

print(result.strftime("วัน %A ประจำวันที่ %d เดือน %B ปี %Y"))

# ว/ด/ป
print(result.strftime("%d / %m / %Y"))
