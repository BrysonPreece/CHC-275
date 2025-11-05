file = open("days1-20.txt", "r")
buffer1_40 = file.readlines()
print(buffer1_40)
file.close()
MFST = []
AMSN = []
NVDA = []
name = []
print(line[0])
for i in buffer1_40:
    line = line.strip()
    line = line.split(",")
    name.append(line[0])
print(name)
print(buffer1_40)