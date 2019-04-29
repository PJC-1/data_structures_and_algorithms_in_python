class Person:
    def __init__(self, name, age):
      self.person_name = name
      self.person_age = age

    def birthday(self):
      self.person_age += 1

    def getName(self):
      name = self.person_name
      return name

bob = Person('Bob', 32)
print(bob.getName())

bob.birthday()
print(bob.person_age)
