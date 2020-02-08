#Hemos usado la clase Student para crear un objeto llamado x.

#¿Cuál es la sintaxis correcta para ejecutar el método printname del objeto x?

class Person:
    def __init__ (self, fname):
        self.firstname = fname

    def printname (self):
        print (self.firstname)
    class Student (Person):
        pass
x = Student("Mike")
x.printname()