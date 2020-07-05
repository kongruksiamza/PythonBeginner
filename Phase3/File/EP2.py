import os
try:
   if os.path.exists("Score.txt"):
       os.remove("Score.txt")
       print("ลบแล้วนะครับ")
   else :
        print("ไม่พบไฟล์นี้ครับผม")
except Exception as e:
    print(e)