# จับคู่คำทักทาย / บุคคล

"""
Hi , Hello 
ก้อง , แก้ม

Hi ก้อง , Hi แก้ม , Hello ก้อง , Hello แก้ม

"""

greeting=["สวัสดี","Hi", "Hello","Good Bye"]
people=["ก้อง","แก้ม","โจ้"]
result=[]
#ลดรูป
result=[x+y for x in greeting for y in people]
print(result)