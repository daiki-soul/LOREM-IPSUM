print("STUDENT GRADE EVAL SYS")

while True:

    try:

        num_students = int(input("How many students are in this class?: "))

        if num_students <= 0:
            raise ValueError("Number of students must be greater than zero.")


#DEFINE STUFF
        total_average   = 0
        passed_count    = 0
        failed_count    = 0


    #START HERE
        print("YOU ARE ENTERING STUDENT GRADES")

        for i in range(1, num_students + 1):

            print("Student {} of {}:".format(i, num_students))

            name = str(input("Name: "))


            while True:
                try:
                    prelim = float(input("Prelim Grade: "))
                    if prelim < 0 or prelim > 100:
                        print("Error: Prelim grade must be between 0 and 100. Try again.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid number for Prelim.")


            while True:
                try:
                    midterm = float(input("Midterm: "))
                    if midterm < 0 or midterm > 100:
                        print("    Error: Midterm grade must be between 0 and 100. Try again.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid number for Midterm.")


            while True:
                try:
                    final_exam = float(input("Final Exam: "))
                    if final_exam < 0 or final_exam > 100:
                        print("Error: Final Exam grade must be between 0 and 100. Try again.")
                        continue
                    break
                except ValueError:
                    print("Error: Please enter a valid number for Final Exam.")


            final_average = (prelim * 0.30) + (midterm * 0.30) + (final_exam * 0.40)
            final_average = round(final_average, 2)

            if 89.9 < final_average <= 100:
                remark = "Excellent"
            elif 84.9 < final_average <= 89:
                remark = "Very Good"
            elif 79.9 < final_average <= 84:
                remark = "Good"
            elif 74.9 < final_average <= 79:
                remark = "Passed"
            else:
                remark = "Failed"


            print(f"Name: {name}")
            print(f"Prelim: {prelim}")
            print(f"Midterm: {midterm}")
            print(f"Final Exam: {final_exam}")
            print(f"Final Average: {final_average}")
            print(f"Remark: {remark}")

            total_average += final_average

            if final_average >= 75:
                passed_count += 1
            else:
                failed_count += 1

        class_average = round(total_average / num_students, 2)


#FINAL OUTPUT HERE
        print("=== Class Summary ===")

        print(f"Total Students: {num_students}")
        print(f"Class Average: {class_average}%")
        print(f"Students Passed: {passed_count}")
        print(f"Students Failed: {failed_count}")

    except ValueError as EHH:
        print("ValueError caught:", EHH)
        print("Please restart this class evaluation.")


    while True:
        again = input("Do you want to evaluate another class? (yes/no): ")
        if again == "yes" or again == "no":
            break
        else:
            print("  Please type 'yes' or 'no' only.")

    if again == "no":
        print("Program terminated. Thank you for using the Grade Evaluation System.")
        break