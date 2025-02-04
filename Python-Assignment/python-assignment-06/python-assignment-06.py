def manage_student_database():
    students = []
    student_id = 1
    while True:
        # Enter Student Name
        student_name = str(input("Please enter the student's name (or type 'stop' to finish): ")).strip()

        # If User want to stop
        if student_name.lower() == 'stop':
            break
        # Check for duplicate names
        if any(student_name.lower() == name.lower() for _, name in students):
            print("This name is already in the list.")
            continue
       
        students.append((int(student_id), student_name))
        student_id += 1 

    print("\nComplete List of Students (Tuples):")
    print(students)

    print("\nList of Students with IDs:")
    for id, name in students:
        print(f"ID: {int(id)}, Name: {name}")

    total_students = len(students)
    print(f"\nTotal number of students: {int(total_students)}")

    total_name_length = sum(len(name) for _, name in students)
    print(f"Total length of all student names combined: {int(total_name_length)}") 
    if students:
        longest_name = max(students, key=lambda x: len(x[1]))[1] 
        shortest_name = min(students, key=lambda x: len(x[1]))[1]  
        print(f"The student with the longest name is: {longest_name}")
        print(f"The student with the shortest name is: {shortest_name}")
manage_student_database()
