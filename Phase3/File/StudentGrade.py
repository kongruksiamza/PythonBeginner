try:
    # fw=open("Score.txt","a",encoding="utf-8")
    # while True:
    #     studentid=input("ป้อนรหัสนักเรียน:")
    #     if studentid == "exit":
    #         break
    #     score=input("ป้อนคะแนนสอบ:")
    #     fw.writelines(studentid+"\t"+score+"\n")
    # fw.close()
    fr=open("Score.txt","r",encoding="utf-8")
    fw=open("Grade.txt","w",encoding="utf-8")
    grade=None
    for line in fr.readlines():
        score=line[-4:].strip() # คะแนนนักเรียน
        studentid=line[:-4].strip() # รหัสนักเรียน
        # print("รหัส = ",studentid," คะแนน = ",score)
        score=int(score)
        if score>=80:
            grade="A"
        elif score>=70 and score<80:
            grade="B"
        elif score>=50 and score<=69:
            grade="C"
        else:
            grade="F"
        fw.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fw.close()
    fr.close()
    
except Exception as e:
    print(e)