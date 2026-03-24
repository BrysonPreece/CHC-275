"""
Name: Bryson Preece
Section: 1
Description: Template for Lab 5
"""



def getStudent(directory, student):

    return (f"The values associated with {student}: {directory[student]}")

def getStudentGrades(directory, student):

    if student in directory:
        return directory[student]['grades']
    else:
        return None

def getStudentGradeLevel(directory,student):
    
    if student in directory:
        gradYear = directory[student]['gradYear']
        current_year = 2026
        grade_level = 12 - (gradYear - current_year)
        return grade_level
    else:
        return None

def getStudentEmail(directory,student):

    if student in directory:
        return directory[student]['email']
    else:
        return None

def getStudentsByGradeLevel(directory, gradelevel):
    
    current_year = 2026
    found = False
    for student, data in directory.items():
        gradYear = data['gradYear']
        gl = 12 - (gradYear - current_year)
        if gl == gradelevel:
            print(student)
            found = True
    if not found:
        print("No students found in that grade level")

def addStudent(directory):

    check1 = True
    while check1 == True:
        name = input("What is the student's name?\n").strip().lower()
        grades = {}
        
        check2 = False
        while check2 == False:
                subject = input("Enter subject:\n").strip()
                try:
                    grade = float(input(f"Enter grade for {subject}:\n").strip())
                    grades[subject] = grade
                except Exception as e:
                    print(f"An error has occurred: {e}")
                input2 = input("Would you like to add another subject(y/n)?\n").strip().lower()
                
                if input2 == 'y':
                    break
                elif input2 == 'n':
                    check2 = True
                else:
                        print("An error has occurred, please try again")
        while check1 == True:
            try:
                gradYear = int(input("Please enter the student's graduation year:\n").strip())
                break
            except Exception as e:
                print(f"An error has occurred: {e}")
        email = input("What is the student's email?\n").strip()
        
        #add to the directory
        directory[name] = {
            'grades': grades,
            'gradYear': gradYear,
            'email': email
        }
        
        print(f"Added student: {name}")
        print(directory)
        
        input1 = input("Would you like to add another(y/n)?\n").strip().lower()
        if input1 == 'y':
            print()
        elif input1 == 'n':
            check1 = False
        else:
            print("An error has occurred, please try again!")
            

def removeStudent(directory, student):

    if student in directory:
        directory.pop(student)
    else:
        print("Student not found")
    print(f"Removed {student}")

def updateGrade(directory, student):
    
    if student not in directory:
        print("Student not found")
        return

    grades = directory[student].get('grades', {})
    check1 = False
    while check1 == False:
        print(f"\nCurrent grades for {student}: {grades}")
        print("1. Add a subject")
        print("2. Remove a subject")
        print("3. Change an existing grade")
        print("4. Quit")
        input1 = input("Enter your selection:\n")
        if input1 == '1':
            subj = input("Enter subject to add: ").strip()
            try:
                grade = float(input(f"Enter grade for {subj}: ").strip())
            except Exception as e:
                print(f"Invalid grade: {e}")
            grades[subj] = grade
            print(f"Added {subj}: {grade}")

        elif input1 == '2':
            subj = input("Enter subject to remove: ").strip()
            if subj in grades:
                grades.pop(subj)
                print(f"Removed {subj}")
            else:
                print("Subject not found")
                
        elif input1 == '3':
            subj = input(f"Which existing grade would you like to change?")
            try:
                grade = float(input(f"Enter grade for {subj}: ").strip())
            except Exception as e:
                print(f"Invalid grade: {e}")
            grades[subj] = grade
            print(f"Added {subj}: {grade}")

        elif input1 == '4':
            check1 = True
            
        else:
            print("An Error has occurred, please try again!")

    directory[student]['grades'] = grades


def calculateGPA(directory, student):

    if student in directory:
        grades = directory[student]['grades']
        if grades:
            GPA = sum(grades.values()) / len(grades)
            return GPA
        else:
            return 0.0
    else:
        return None


def checkHonorRoll(directory,student):
 
    if student in directory:
        gpa = calculateGPA(directory, student)
        grades = directory[student]['grades']
        if gpa >= 88 and all(grade > 81 for grade in grades.values()):
            return True
        else:
            return False
    else:
        return False

def printMenu():
  
    print("\n***********************************************************")
    print("Welcome to the statistics Calculator!")
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. Get Student")
    print("4. Update Grades")
    print("5. Calculate GPA")
    print("6. Print Students by grade level")
    print("7. Quit")
    input1 = input("Please enter your selection: ").strip()
    print("***********************************************************\n")
    return input1

    pass

def main():
    students = {}
    check1 = False
    while check1 == False:
        input1 = printMenu()
        if input1 == '1':
            addStudent(students)
            print(students)
        elif input1 == '2':
            input2 = input("Which student would you like to remove?:\n").lower().strip()
            removeStudent(students, input2)
        elif input1 == '3':
            input3 = input("Which student's directory would you like to access?:\n").lower().strip()
            print(getStudent(students, input3))
        elif input1 == '4':
            input4 = input("Which student would you like to update the grades for?:\n").lower().strip()
            updateGrade(students, input4)
        elif input1 == '5':
            input5 = input("Which student would you like to calculate GPA for?:\n").lower().strip()
            gpa = calculateGPA(students, input5)
            if gpa is not None:
                print(f"GPA for {input5}: {gpa:.2f}")
            else:
                print("Student not found")
        elif input1 == '6':
            try:
                gl = int(input("Enter grade level:\n").strip())
                getStudentsByGradeLevel(students, gl)
            except ValueError:
                print("Invalid grade level")
        elif input1 == '7':
            check1 = True

if __name__ == "__main__":
    main()