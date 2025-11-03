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
