class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.age = age
        self.gender = gender
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'Name: {self.first_name} {self.last_name}, Gender: {self.gender}, Age: {self.age}'
