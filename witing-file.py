def writeFile():
    with open('fileExample1.txt','w') as myFile:
        myFile.write("I never saw a purple cow")
        myFile.write("\n")
        myFile.write("I hope I never see one")
        myFile.write("\n")
        myFile.close()
writeFile() 

def writeFile3():
    with open('fileExample1.txt','a') as myFile:
        myFile.write("\n")
        myFile.write("\n")
        myFile.write("This poem is by Lucas Dorey")
        myFile.write("\n")
        myFile.close()
writeFile3() 
