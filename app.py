class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def display_info(self):
        return f"name: {self.name}, surname: {self.surname}, age: {self.age}"


class Student(Person):
    def __init__(self, name, surname, age, university):
        super().__init__(name, surname, age)
        self.university = university

    def display_info(self):
        person_info = super().display_info()
        return f"{person_info}, university: {self.university}"


class PersonMixin:
    def display_info(self):
        attributes = ", ".join([f"{key}: {value}" for key, value in self.__dict__.items()])
        return attributes


# Add the mixin to the Person class
class PersonWithMixin(PersonMixin, Person):
    pass


# Add the mixin to the Student class
class StudentWithMixin(PersonMixin, Student):
    pass


# Example usage
person = PersonWithMixin(name="John", surname="Doe", age=25)
student = StudentWithMixin(name="Jane", surname="Smith", age=22, university="XYZ University")

print(person.display_info())
print(student.display_info())

    

