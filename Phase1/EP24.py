#แปลงอุณหภูมิ
temp = input("ป้อนอุณหภูมิ (องศา) :") #45C

degree= int(temp[:-1]) #45
unit=temp[-1].upper() #C


if unit=="C":
    result=(9*degree)/5+32
    unit_result="ฟาเรนไฮน์"
if unit=="F":
    result=(degree-32)*5/9
    unit_result="เซลเซียส"

print("แปลงตัวเลข = ",temp," เป็น ",unit_result," = ",result)