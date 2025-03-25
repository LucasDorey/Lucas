def students():
    myFile =open('fileExample1.txt','w')
    myFile.write("Michael")
    myFile.write("\n")
    myFile.write("Alex")
    myFile.write("\n")
    myFile.write("Jo")
    myFile.write("\n")
    myFile.write("Robin")
    myFile.write("\n")
    myFile.write("Max")
    myFile.write("\n")
    myFile.write("George")
    myFile.write("\n")
    myFile.close()
students() 

def Listy():
    with open("fileExample1.txt","r") as File:
        student_register = File.readlines()
    list.sort()
    print(student_register)

Listy()

with open('fileExample1','r') as file:
    studentsArray = file.readlines()

studentsArray.sort()

for student in studentsArray:
    print(student, end = "")