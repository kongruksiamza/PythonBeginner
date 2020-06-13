# **kwargs 

# *args => ค่าใน parameter มีได้หลายค่า
def add(*number):
    sum=0
    for i in range(len(number)):
        sum+=number[i]
    print(sum)

#ชื่อ Parameter มีหลายชื่อ
def displayData(**item):
    print(item)


displayData(fname="Kong",lname="Ruksiam")
displayData(fname="Kong",lname="Ruksiam",city="กรุงเทพ")
displayData(fname="Kong",lname="Ruksiam",status="โสด")
displayData(fname="Kong",lname="Ruksiam",age=20,city="กรุงเทพ",status="แต่งงาน")
displayData(fname="Kong",lname="Ruksiam",age=20,city="กรุงเทพ",status="แต่งงาน",job="Programmer")
displayData(fname="Kong")
displayData(fname="Kong",lname="Ruksiam",country="ระยอง")