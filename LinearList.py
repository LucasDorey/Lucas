my_list = [3, 15, 2, 16, 11]
slush = input("What is your number?")
slush = int(slush)
for i in range(5):
    if my_list[i] == slush:
        print('')
        print("Your number has been found")

    else:
        print("Your number has not been found")
        break



