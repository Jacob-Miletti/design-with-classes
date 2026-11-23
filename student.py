"""
This module defines a Student class with comparison methods for equality,
 less than, and greater than or equal to. It also includes a main function
that demonstrates the usage of the Student class
 """
import random


class Student:
    def __init__(self, name: str) -> None:
        self.name = name

    def __eq__(self, other: "Student") -> bool:
        return self.name == other.name

    def __lt__(self, other: "Student") -> bool:
        return self.name < other.name

    def __ge__(self, other: "Student") -> bool:
        return self.name >= other.name


def main() -> None:
    student1 = Student("Alice")
    student2 = Student("Bob")
    student3 = Student("Alice")

    print(f"{student1.name} == {student3.name}: {student1 == student3}")
    print(f"{student1.name} < {student2.name}: {student1 < student2}")
    print(f"{student2.name} >= {student1.name}: {student2 >= student1}")

    students = [
        Student("Maya"),
        Student("Carlos"),
        Student("Ava"),
        Student("Jordan"),
        Student("Liam"),
        Student("Alice"),
        Student("Bob"),
    ]
    random.shuffle(students)
    students.sort()

    print("\nStudents sorted by name:")
    for student in students:
        print(f"Name: {student.name}")


if __name__ == "__main__":
    main()