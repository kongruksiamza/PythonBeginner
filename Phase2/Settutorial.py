#แบบปกติ
fruit={"มะม่วง","มะขาม","มะยม"}

#เพิ่มข้อมูลสมาชิก
fruit.add("ทุเรียน")
fruit.add("สัปปะรด")
fruit.add(999)
#เพิ่มสมาชิกหลายตัว
fruit.update(["ตะไคร้","โหระพา","ชะอม"])

#Loop
print(fruit)

#แสดงจำนวนสมาชิกใน set
# print(len(fruit))

fruit.discard("ทุเรียน") # remove / discard
del fruit
print(fruit)