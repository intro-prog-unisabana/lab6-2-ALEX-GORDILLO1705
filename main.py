from grades_manager import *

def main():
    my_grades = {}

    print("Welcome to the Student Grades Manager!\n")

    while True:
        print("Select an option:")
        print("1. Add a student")
        print("2. Print student grade averages")
        print("3. Exit")

        choice = input()

        if choice == "1":
            my_grades = add_student(my_grades)

        elif choice == "2":
            print("Select an option:")
            print("a. Display all students")
            print("b. Display selected students")

            sub_choice = input()

            if sub_choice == "a":
                avg_by_student(my_grades)

            elif sub_choice == "b":
                names = input("Enter student names (comma-separated): ")
                keys = [name.strip() for name in names.split(",")]
                avg_by_student(my_grades, keys)

            else:
                print("Invalid option selected!")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid option selected!")

if __name__ == "__main__":
    main()