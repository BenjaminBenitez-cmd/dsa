class Person:

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def getName(self):
        return self.firstname + " " + self.lastname

    def getAge(self):
        return self.age


class Student(Person):
    def __init__(self, firstname, lastname, age, year, gpa):
        super().__init__(firstname, lastname, age)

        self.graduationyear = year
        self.gpa = gpa

    def getGPA(self):
        return self.gpa

    def getGraduationyear(self):
        return self.graduationyear


class Faculty(Person):
    def __init__(self, firstname, lastname, age, subject, designation):
        super().__init__(firstname, lastname, age)

        self.subject = subject
        self.designation = designation

    def getSubject(self):
        return self.subject

    def getDesignation(self):
        return self.designation


def main():
    john = Student("John", "Doe", 23, 2001, 4.00)
    tom = Faculty("Tom", "Jones", 43, "Electrical Engineering", "Professor")
    print(tom.getName())
    print(john.getGPA())


main()
