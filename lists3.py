mylist = ["John Cardinal", 12, 88, "CardinalJ26@chcstudent.com"]
names = ["John", "Paul", "Luke"]
gradelevels = [12, 11, 10]
GPAas = [90, 74, 65]
print(f"Student records for {names[0]}. Gradelevel: {gradelevels[0]}. GPA {GPAas[0]}")
for i in range(len(names)):
    print(f"Student records for {names[i]}. Gradelevel: {gradelevels[i]}. GPA {GPAas[i]}")
    