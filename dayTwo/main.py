subDepth = 0
subPosition = 0
finalPosition = 0

fileInput = open("input.txt", "r")
for line in fileInput:
    x = line.split(" ")
    if x[0] == "forward":
        subPosition += int(x[1])
    elif x[0] == "down":
        subDepth += int(x[1])
    elif x[0] == "up":
        subDepth -= int(x[1])

fileInput.close()

finalPosition = subPosition * subDepth
print(finalPosition)




