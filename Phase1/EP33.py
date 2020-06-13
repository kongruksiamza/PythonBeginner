#สร้างภาพวาด 4 เหลี่ยมจตุรัส

"""
3x3
xxx
xxx
xxx

2x2
xx
xx

5x5
xxxxx
xxxxx
xxxxx
xxxxx
xxxxx

"""

number=int(input("ป้อนขนาด  = ")) # 5 => 0,1,2,3,4

"""

"""
for row in range(number) :
    for column in range(number):
        print("x",end="")
    print(" ")
