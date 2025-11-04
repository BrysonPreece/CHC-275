file = open("names.txt", "r")
# r = read mode, w = write mode. X = overwrite
buffer = file.readlines() # read buffer into a list
print(buffer) # print file
file.close() # close file
names = []
grades = []
for line in buffer:
    line = line.strip() # Removes all excess white space
    line = line.split(",") #Split our line by the comma
    #Line is now list of 2 objects line [0] is name and line [1] is grade
    names.append(line[0])
    line[1] = int(line[1])
    grades.append(line[1])
print (names)
print (grades)
#txt is formatted 
#Name, GPA
#Data type for Name: String
#Data type for Grade: Int
names.append("Oden")
grades.append(21)
file = open("names.txt","w") #  Write mode
line = "hello world"
file.write(line)
file.close()
"{name}, {grade}\n" #This is the structure
file = open("names.txt","w")
buffer = []
for i in range(len(names)):
    line = f"{names[i]},{grades[i]}\n"
    buffer.appned(line)
buffer [-1] = buffer[-1].strip()
file.writelines(buffer)
file.close
try:
    name = input("Enter your name")
    grade = input("Enter your grade:")
    grade = int(grade)
except Exception as e:
    print(e)
else:
    file = open("names.txt","a")
    line = f"{name},{grade}"
    file.write(line)
    file.close
date = "March52025"
file = open(date, "w")
avg = sum(grades)/len(grades)
line = f"The average GPA on {date} is {avg}"
file.write(line)
file.close()