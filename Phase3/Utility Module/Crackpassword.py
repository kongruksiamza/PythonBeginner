# รหัส ATM = 132
import random

ATM_PASSWORD="ko6"
result="" #สำหรับเก็บผลลัพธ์

while result!=ATM_PASSWORD :
      result="" 
      for letter in range(len(ATM_PASSWORD)):
          list_number=random.choice("0123456789abcdefghijklmnopqrstuvwxyz")
          result="".join(list_number)+str(result)
          print("SEARCH = ",result)
print("CRACK PASSWORD IS ", result)