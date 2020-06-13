# function return ค่า

def randomNumber(x):
    if len(x)<3 :
        return
        
    if x == "100":
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย")
        return 0


money=randomNumber("100")
print("เงินรางวัล = ",money)