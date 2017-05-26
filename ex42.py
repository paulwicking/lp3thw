## Animal is-a object
class Animal(object):
	pass

## Dog is-a Animal
class Dog(Animal):
	def __init__(self, name):
		## Dog has-a name
		self.name = name

## Cat is-a animal
class Cat(Animal):
	def __init__(self, name):
		## Cat has-a name
		self.name = name

## Person is-a object
class Person(object):
	def __init__(self, name):
		## Person has-a name
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a person
class Employee(Person):
	def __init__(self, name, salary):
		## super() == what??
		super(Employee, self).__init__(name)

		## Employee has-a salary
		self.salary = salary

## Fish is-a object
class Fish(object):
	pass

## Salmon is-a Fish
class Salmon(Fish):
	pass

## Halibut is-a Fish also
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## mary has-a satan (mary's pet is-a satan)
mary.pet = satan

## frank is-a employee that has-a salary
frank = Employee("Frank", 120000)

## frank has-a pet (frank's pet is-a rover)
frank.pet = rover

## flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
