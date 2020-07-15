"""
class Dog:

    species = 'Mammal'

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    def bark(self, number):
        print('WOOF! My name is {} and the number is {}'.format(self.name, number))


my_dog = Dog('Lab', 'Framkei')
"""
#my_dog.bark(10)

class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius
        self.area = radius *radius *self.pi

    def get_cicumference(self):
        return  self.radius * self.pi * 2

my_circle = Circle(30)
#print(my_circle.area)


class Animal:
    def __init__(self):
        print('ANIMAL CREATED')

    def whoami(self):
        print('I am an animal')

    def eat(self):
        print('I am eating')

#my_animal= Animal()

#my_animal.whoami()

class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print('Dog Created')

    def eat(self):
        print(('I am a dog and earing'))

    def bark(self):
        print('WOOf')

#my_dog = Dog()

#my_dog.bark()



class Book:
    def __init__(self, title, author, pages):

        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages


b = Book('Python rocks', 'Jose', 200)