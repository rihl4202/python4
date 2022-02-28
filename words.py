intro = input("Introduce Yourself: ")
count = 0
words = 1
for i in intro:
    count = count+1
    if(i == " "):
        words = words+1
        count = count-1
print(count)
print(words)