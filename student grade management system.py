# Function to calculate total score and grade
def calculate_grade(scores):
    total_score = sum(scores)
    average_score = total_score / len(scores)

    if average_score >= 90:
        grade = 'A'
    elif 80 <= average_score < 90:
        grade = 'B'
    elif 70 <= average_score < 80:
        grade = 'C'
    elif 60 <= average_score < 70:
        grade = 'D'
    else:
        grade = 'F'

    return total_score, grade


# Function to display all students' details
def display_students(students):
    print("\nStudent Details:")
    for student in students:
        total_score, grade = calculate_grade(student['scores'])
        print(f"Name: {student['name']}, ID: {student['id']}, Total Score: {total_score}, Grade: {grade}")


# Main script to manage student data
def main():
    students = []

    while True:
        # Collect student data
        name = input("Enter student's name: ")
        student_id = input("Enter student's ID: ")
        scores = []
        for i in range(3):  # Input scores for 3 subjects
            score = float(input(f"Enter score for subject {i + 1}: "))
            scores.append(score)

        # Add student to the list
        student_data = {'name': name, 'id': student_id, 'scores': scores}
        students.append(student_data)

        # Check if more students need to be added
        more_students = input("Do you want to add another student? (yes/no): ").lower()
        if more_students != 'yes':
            break
    # Display all student data
    display_students(students)


# Run the main function
if __name__ == "__main__":
    main()
