#1 ==============
"""
from tabulate import tabulate
variables = {
    "name": "Aminul Islam",
    "age": 51,
    "gpa": 3.75,
    "is_student": True,
}
table = [(k, repr(v), type(v).__name__) for k, v in variables.items()]
print(tabulate(table, headers=["Variable", "Value", "Type"], tablefmt="fancy_grid"))
"""

#2 ================


def get_valid_input(prompt, input_type=str, validation_func=None):
    # et validated input from user with error handling.
    while True:
        try:
            user_input = input(prompt).strip()
            if input_type != str:
                user_input = input_type(user_input)

            if validation_func and not validation_func(user_input):
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")


class StudentGradingSystem:
    # A professional student grading system with GPA calculation.

    # Grading scale with GPA points
    GRADING_SCALE = {
        'A+': {'min': 90, 'max': 100, 'gpa': 5.0},
        'A': {'min': 80, 'max': 89, 'gpa': 4.0},
        'A-': {'min': 70, 'max': 79, 'gpa': 3.5},
        'B': {'min': 60, 'max': 69, 'gpa': 3.0},
        'C': {'min': 50, 'max': 59, 'gpa': 2.0},
        'D': {'min': 40, 'max': 49, 'gpa': 1.0},
        'F': {'min': 0, 'max': 39, 'gpa': 0.0}
    }

    # Subject definitions
    COMPULSORY_SUBJECTS = [
        'English 1st Paper', 'English 2nd Paper',
        'Bangla 1st Paper', 'Bangla 2nd Paper',
        'Mathematics', 'Islamic Education'
    ]

    SCIENCE_SUBJECTS = [
        'Physics', 'Chemistry', 'Biology', 'Higher Mathematics'
    ]

    ARTS_SUBJECTS = [
        'Economics', 'Civics', 'Geography', 'General Science'
    ]

    COMMERCE_SUBJECTS = [
        'Accounting', 'Business Studies', 'Finance', 'Statistics'
    ]

    def __init__(self):
        self.student_data = {}

    def get_student_info(self):
        """Collect  # noinspection PyStatementEffect
comprehensive student information."""
        print("\n=== STUDENT INFORMATION ===")

        self.student_data['name'] = get_valid_input("Enter student name: ")
        self.student_data['roll_no'] = get_valid_input("Enter roll number: ")

        # Group selection
        groups = ['Science', 'Arts', 'Commerce']
        print("\nAvailable groups:")
        for i, group in enumerate(groups, 1):
            print(f"{i}. {group}")

        group_choice = get_valid_input(
            "Select group (1-3): ",
            int,
            lambda x: 1 <= x <= 3
        )
        self.student_data['group'] = groups[group_choice - 1]

    def get_subject_marks(self):
        """Collect marks for all relevant subjects based on group."""
        print(f"\n=== ENTER MARKS FOR {self.student_data['group'].upper()} GROUP ===")
        self.student_data['subjects'] = {}

        # Compulsory subjects for all groups
        print("\n--- COMPULSORY SUBJECTS ---")
        for subject in self.COMPULSORY_SUBJECTS:
            marks = get_valid_input(
                f"Enter marks for {subject} (0-100): ",
                int,
                lambda x: 0 <= x <= 100
            )
            self.student_data['subjects'][subject] = marks

        # Group-specific subjects
        print(f"\n--- {self.student_data['group'].upper()} GROUP SUBJECTS ---")
        group_subjects = getattr(self, f"{self.student_data['group'].upper()}_SUBJECTS")

        for subject in group_subjects:
            marks = get_valid_input(
                f"Enter marks for {subject} (0-100): ",
                int,
                lambda x: 0 <= x <= 100
            )
            self.student_data['subjects'][subject] = marks

    def calculate_grade_and_gpa(self, marks):
        """Calculate grade and GPA based on marks."""
        for grade, criteria in self.GRADING_SCALE.items():
            if criteria['min'] <= marks <= criteria['max']:
                return grade, criteria['gpa']
        return 'F', 0.0

    def calculate_overall_performance(self):
        """Calculate overall GPA and performance."""
        total_marks = 0
        total_gpa = 0
        subject_count = len(self.student_data['subjects'])

        self.student_data['subject_results'] = {}

        for subject, marks in self.student_data['subjects'].items():
            grade, gpa = self.calculate_grade_and_gpa(marks)
            self.student_data['subject_results'][subject] = {
                'marks': marks,
                'grade': grade,
                'gpa': gpa
            }
            total_marks += marks
            total_gpa += gpa

        self.student_data['total_marks'] = total_marks
        self.student_data['average_marks'] = total_marks / subject_count
        self.student_data['cgpa'] = total_gpa / subject_count

        # Calculate overall grade based on average marks
        avg_grade, _ = self.calculate_grade_and_gpa(self.student_data['average_marks'])
        self.student_data['overall_grade'] = avg_grade

    def get_congratulatory_message(self):
        """Generate appropriate congratulatory message based on performance."""
        cgpa = self.student_data['cgpa']

        if cgpa >= 4.5:
            return "🎉 Outstanding Achievement! Congratulations on your exceptional performance! 🎉"
        elif cgpa >= 4.0:
            return "🌟 Excellent Work! Congratulations on your outstanding results! 🌟"
        elif cgpa >= 3.5:
            return "👍 Great Job! Congratulations on your excellent performance! 👍"
        elif cgpa >= 3.0:
            return "👏 Well Done! Congratulations on your good results! 👏"
        elif cgpa >= 2.0:
            return "✅ Good Effort! Congratulations on passing! ✅"
        else:
            return "💪 Keep Trying! Congratulations on your endeavor and don't give up! 💪"

    def display_results(self):
        """Display comprehensive results in a professional format."""
        print("\n" + "=" * 60)
        print("STUDENT GRADE REPORT".center(60))
        print("=" * 60)

        print(f"Student Name: {self.student_data['name']}")
        print(f"Roll Number: {self.student_data['roll_no']}")
        print(f"Group: {self.student_data['group']}")

        print("\n" + "-" * 60)
        print(f"{'SUBJECT':<25} {'MARKS':<8} {'GRADE':<6} {'GPA':<6}")
        print("-" * 60)

        for subject, result in self.student_data['subject_results'].items():
            print(f"{subject:<25} {result['marks']:<8} {result['grade']:<6} {result['gpa']:<6.1f}")

        print("-" * 60)
        print(f"\nSUMMARY:")
        print(f"Total Marks: {self.student_data['total_marks']}")
        print(f"Average Marks: {self.student_data['average_marks']:.2f}")
        print(f"Overall Grade: {self.student_data['overall_grade']}")
        print(f"CGPA: {self.student_data['cgpa']:.2f}")
        print("=" * 60)

        # Display congratulatory message
        congrat_message = self.get_congratulatory_message()
        print(f"\n{congrat_message}")
        print("Congratulations for your endeavor!".center(60))
        print("=" * 60)

    def display_grading_scale(self):
        """Display the grading scale for reference."""
        print("\nGRADING SCALE REFERENCE:")
        print("-" * 40)
        print(f"{'GRADE':<6} {'MARKS RANGE':<15} {'GPA':<6}")
        print("-" * 40)
        for grade, criteria in self.GRADING_SCALE.items():
            print(f"{grade:<6} {criteria['min']}-{criteria['max']:<13} {criteria['gpa']:<6.1f}")

    def run(self):
        """Main method to run the grading system."""
        print("Welcome to Student Grading System")
        print("=" * 40)

        self.display_grading_scale()
        self.get_student_info()
        self.get_subject_marks()
        self.calculate_overall_performance()
        self.display_results()


def main():
    """Main function to initialize and run the grading system."""
    try:
        grading_system = StudentGradingSystem()
        grading_system.run()
    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
