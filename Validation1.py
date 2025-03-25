def getTest():
    invalidTest = True
    while invalidTest:
        score = input("Enter the percentage you got in the test: ")
        if not score.isdigit():
            print("Your score can only contain numbers")
        else:
            score = int(score)
            if 0 <= score <= 100:
                invalidTest = False
            else:
                print("Please enter a score between 0 and 100.")
    return score
            

score = getTest()
print("Your valid score was: ", score)