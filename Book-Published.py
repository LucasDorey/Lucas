def library():
    book = str(input("What is the name of your book: "))
    year = str(input("What is the year your book was published: "))
    book = book[0:3]
    year = year[2:4]

    code = book + year

    print("Your code is:", code)

library()
