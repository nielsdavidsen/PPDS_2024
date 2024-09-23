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



