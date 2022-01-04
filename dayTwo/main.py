subDepth = 0
subPosition = 0

fileInput = open("input.txt", "r")
for line in fileInput:
    x = line.split(" ")
    print(int(x[1]))
# commandInputs = fileInput.read()


fileInput.close()





