#Create a "Person" class

class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

p0 = Person("Umidjon", "Otaqulov", 19)
print(p0.first_name)