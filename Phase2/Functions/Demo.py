def hanoi (n,a,b,c):
    if n==0 :
        return
    hanoi(n-1,a,c,b)
    print("ย้าย = ",n ," จาก = ",a ," ไป = ",c)
    hanoi(n-1,b,a,c)

hanoi(3,"A","B","C")