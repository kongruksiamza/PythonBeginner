# Global Variable / Local Variable

def displayNumber():
    x=50
    a=100
    print("Hello = ",a," ใน")


#โปรแกรมหลัก
a=200
displayNumber()
print("นอก = ",a)

# นาย x ดารา => x ทั่วประเทศรู้จัก (Global)
# นาย x หมู่บ้านแสนสุข => x ในหมู่บ้าน (Local)