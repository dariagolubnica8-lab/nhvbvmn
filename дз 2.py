class Animal:
    def sound(self):
        print("Тварина робить звук")
class Dog(Animal):
    def bark(self):
        print("гав гав")
class Cat(Animal):
    def meow(self):
        print("мяу")
dog = Dog()
dog.sound()
dog.bark()
cat = Cat()
cat.sound()
cat.meow()