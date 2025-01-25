from student import Student
from group import Group
from student_limit_error import StudentLimitError

def main():
    st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
    st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
    gr = Group('PD1')
    print(gr)

    gr.delete_student('Taylor')

    try:
        gr.add_student(st1)
        gr.add_student(st2)

    except StudentLimitError as error:
        print(error)
    except Exception as error:
        print(error)

    print(gr)
    assert gr.find_student('Jobs') == st1  # 'Steve Jobs'
    assert gr.find_student('Jobs2') is None


if __name__ == "__main__":
    main()
