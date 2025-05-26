"""
This module defines the Student class and demonstrates its usage.
It handles student grades, calculating averages, honor status, and reports.
"""

class Student:
    """Class representing a student with grades and status."""

    def __init__(self, identification: str, name: str):
        """
        Initialize a student with an ID and a name.
        Grades are stored in a list.
        """
        self.identification = identification
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = False

    def add_grade(self, grade):
        """
        Add a grade if it is a valid numeric value between 0 and 100.

        Args:
            grade (int or float): Grade to add.
        """
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print(f"Ignored invalid grade: {grade}")

    def calculate_average(self):
        """
        Calculate and return the average of the grades.
        Returns None if there are no grades.

        Returns:
            float or None: Average grade or None if no grades exist.
        """
        if not self.grades:
            return None
        return sum(self.grades) / len(self.grades)

    def check_honor(self):
        """
        Check if the student qualifies for honors.
        Honors is True if average grade is above 90, otherwise False.
        """
        avg = self.calculate_average()
        if avg is not None and avg > 90:
            self.honor = True
        else:
            self.honor = False

    def delete_grade(self, index):
        """
        Delete the grade at the specified index if it exists.

        Args:
            index (int): Index of the grade to delete.
        """
        try:
            del self.grades[index]
        except IndexError:
            print(f"Index out of range: {index}")

    def report(self):
        """
        Print a report with the student's ID, name, grades count,
        average grade, honor status, and pass status.
        """
        avg = self.calculate_average()
        avg_str = f"{avg:.2f}" if avg is not None else "N/A"
        print(f"ID: {self.identification}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average Grade: {avg_str}")
        print(f"Honor: {'Yes' if self.honor else 'No'}")
        print(f"Passed: {'Yes' if self.is_passed else 'No'}")

    def check_passed(self, passing_grade=60):
        """
        Update the pass status based on whether the average grade
        meets or exceeds the passing grade.

        Args:
            passing_grade (int or float, optional): Threshold for passing.
                Defaults to 60.
        """
        avg = self.calculate_average()
        if avg is not None and avg >= passing_grade:
            self.is_passed = True
        else:
            self.is_passed = False

def startrun():
    """
    Demonstrates usage of the Student class.
    Adds grades, checks pass and honor status, deletes a grade,
    and prints a report.
    """
    student = Student("x123", "John Doe")
    student.add_grade(100)
    student.add_grade("Fifty")
    student.add_grade(75)

    student.check_passed()
    student.check_honor()

    student.delete_grade(5)

    student.report()


if __name__ == "__main__":
    startrun()
