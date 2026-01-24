
def valid_marks():
    while True:
        try:
            marks = float(input("Enter the student's grade (0 - 100): "))
            if 0<= marks <= 100:
                return marks
            else:
                print("Invalid input. Please enter a marks between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_grade(marks):
    if 90 <= marks <= 100:
        return "A", "Excellent!"
    elif 80 <= marks <= 89:
        return "B", "Very Good! keep it up! \U0001F44D"
    elif 70 <= marks <= 79:
        return "C", "Good!"
    elif 60 <= marks <= 69:
        return "D", "Pass!"
    else: 
        return "F", "Fail. Do better next time!"

print("Student Grade Calculator\n")
def main():
    student_name = input("Enter the student's name: ")
    
    marks = valid_marks()
    grade, message = calculate_grade(marks)
    
    print(f"\nResult for {student_name.upper()}: ")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

if __name__ == "__main__":
    main()