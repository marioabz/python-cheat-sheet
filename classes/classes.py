
# Classes
# Classes are defined with the reserved word 'class' besides the class name.
# There should be 2 blank lines between functions and between classes.
# There should be 1 blank line between methods inside a class definition.
# A subclass can derive from a parent/base class, inheriting its behavior 
# and making behavior specific to the sub-class.
class A():
    pass

class B(A):
    pass

class C(B):
    pass


class NationalId(object):

    # Class attribute
    id_offset = 884565855

    # Initializing function
    def __init__(self, state: int):

        # Instance attributes
        self.state = state
        self.citized_id = NationalId.id_offset
        NationalId.id_offset += 1

    # Instance attribute. Method to get user ID.
    def get_id(self):
        return "{}#{}".format(self.state, self.citizen_id)


# Collaborating classes
# Tell, dont ask. Tell object what to do, dont ask for their state

# Polymorphism: using objects of different types through a common interface
# Duck typing
class Mexico():
    
    def get_population(self) -> int:
        return int(16*10e6)


class India():
    
    def get_population(self) -> int:
        return int(1.366*10e8)


# Function 'print_country_population' doesn't care about the instance type.
def print_country_population(instance):
    print(instance.get_population())


# Inheritance.
# Parent class
class Rectangle(object):

    def __init__(self, length, width):
        self.width = width
        self.length = length
    
    def get_area(self):
        return self.length * self.width
    
    def get_perimeter(self):
        return 2*(self.width + self.length)


#Class 'Square' is a subclass of 'Rectangle'
class Square(Rectangle):

    def __init__(self, length):
        super().__init__(length, length)


#Class 'Cube' is a subclass of 'Square'
class Cube(Square):
    
    def get_superficial_area(self) -> int:
        return super().get_area() * 6
    
    def get_volume(self) -> int:
        return self.length **3


class Person(object):

    def __init__(self, name, surname, age, height):
        self.name = name
        self.surname = surname
        self.age = age
        self.height = height

    def __call__(self, delimeter):
        length = 65
        print(length * delimeter)
        print(self.__dict__)
        print(length * delimeter)

    def __len__(self):
        return int(float(self.height[:-1])*100)


# The 'property' decorator allows to set attributes,
# setters, getters, and deleters in a pythonic way
class Server(object):

    def __init__(self, ip, port):
        self._ip = ip
        self._port = port

    @property
    def ip(self):
        print("Querying ip...")
        return self._ip

    @property
    def port(self):
        print("Querying port...")
        return self._port
    
    @port.setter
    def port(self, port):
        print("Setting port")
        self._port = port


a = Square(5)
print(a.get_area(), a.get_perimeter())

print_country_population(India())
print_country_population(Mexico())

print(Cube(5).get_superficial_area(), Cube(3).get_volume())

mario = Person(name="Mario", surname="Briseño", age=25, height="1.76m")
mario("*")
print(len(mario), "centimeters of height")

server = Server("localhost", 8080)
print(server.port, server.ip)
server.port = 5000
print(server.port)