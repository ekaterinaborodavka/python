from student_limit_error import StudentLimitError

class Group:

    def __init__(self, number, limit_student = 10):
        self.number = number
        self.group = set()
        self.limit_student = limit_student

    def add_student(self, student):
        if len(self.group) == self.limit_student:
            raise StudentLimitError(f"Student limit exceeded. Only {self.limit_student} students allowed.")
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\\n {all_students} '