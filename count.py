def counting():
    filename = input("Enter File Name: ")
    file = open(filename, "r")
    count = 0
    for i in file:
        words = i.split()
        count = count+len(words)
    print(count)
counting()