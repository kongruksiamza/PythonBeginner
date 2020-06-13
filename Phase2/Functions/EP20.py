#tower of hanoi

def hanoi(n,a,b,c):
    if(n==0):
        return
    hanoi(n-1,a,c,b) 
    print("จานที่  = ",n ,"จาก =  ",a," ไป = ",c)
    hanoi(n-1,b,a,c)

hanoi(4,"A","B","C")