#a class is a specifications of how an object should be built. It is a blueprint for objects (which attributes it has).

#an object built from a class is an instance of that class. 

#we can create an object from a class by calling the class like a function.

æ = str(8) #creates a string from an integer

å = tuple([1,2,3]) #creates a tuple from a list

#When creating a class, it contains two parts: data attributes and methods. The method takes "self" as first argument.
#EXAMPLE OF STRUCTURE OF A CLASS:
class class_name:

    def __init__(self, attribute1, attribute2):
        '''SETTING UP THe attributes through a constructor'''
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def method(self):
        '''constructing a method'''
        return self.attribute1 + self.attribute2


#my own class

class my_info:

    def initialized(self, firstname, lastname, age):
        '''setting up the attributes'''
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print(self):
        return print('Name: ' + self.firstname + self.lastname + '\nAlder: ' + str(self.age))

#testing my class
infos = my_info()
infos.initialized('Anso', 'Maxen', 24)
infos.print()

#Changing the my_info class to use a constructor instead of a method

class MyInfo:

    def __init__(self, firstname, lastname, age):
        '''setting up the attributes'''
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print(self):
        return print('Name: ' + self.firstname + ' ' + self.lastname + '\nAlder: ' + str(self.age))

#testing my class
info = MyInfo('Anso', 'Maxen', 24)

info.print()

#new classes, now using inheritance. 


class Person:

    def __init__(self, name, cpr, address):
        self.name = name
        self.cpr = cpr
        self.address = address


class Student(Person):

    def __init__(self, name, cpr=0, address='none', student_id=1):  #you still need to add all the same attributes as the base-class
        super().__init__(name, cpr, address)             #here comes the inheritance
        self.student_id = student_id


#testing the underclass
stud = Student('Ac', 1234, 'sted', 'dhv202')

print(stud.address)


#class of students

class StudentGroup:
    def __init__(self, students=[]):
        '''Constructor. The list of students is optional'''
        self.students = students

    def add_student(self, student):
        '''Constructor. Add a new student to the group'''
        self.students.append(student)

    def get_names(self, students):

        for student in students:
            print(student.name)


#testing my group-maker
albert = Student(name="Albert Einstein",
                 cpr="14031879-1235") 

ac = Student(name="AC", cpr="123456-1234")

group = StudentGroup()

group.students.append(albert)
group.students.append(ac)

group.get_names(group.students)

