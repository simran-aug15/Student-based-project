student={}


while True:
    print("\n---- STUDENT MANAGER APP---")
    print("1. Add Student")
    print("2. View Student")
    print("3. Check Result")
    print("Exit")

    choice=input("Enter your choice")


    #Add student
    if choice=="1":
        name=input("Enter student name: ")
        marks=marks(input("Enter the marks: "))
        student[name]=marks
        print(f"{name} Successfully added !")
              
    #view student
    elif choice=="2":
        if not student:
            print("No student found! ")
        else:
          for name, marks in student.items():
            print(name, ":",marks)  

    #check result
    elif choice=="3":
      name = input("Enter student name: ")

      if name in student:
        print("Marks:", student[name])
      else:
        print("Student not found")
                     


       
