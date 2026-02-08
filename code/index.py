class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

p1 = Person(18, "daiki")
p2 = Person("Alex", 20)

p1.greet()
p2.greet()
