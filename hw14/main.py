# Task 14.1
class StudentLimitError(Exception):
    def __init__(self, error_message):
        self.error_message = error_message

class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, Record Book: {self.record_book}'

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr.group)

