# This is the firt trial of the python code using the sublime tyext and the following i what i will  be implementing as  i aTm coding
print("This is the implementation of the class and methods") 
class Dog:
	def bark(self):
		print("The dog barks")

dog = Dog()
dog.bark()

class student:
	def __init__(self,name,age,course):
		self.name = name
		self.age =age 
		self.course = course 
		self.varsity= None
		self.course= None
	def scholarship(self,varsity, country):
		self.varsity = varsity
		self.country = country



me = student("Danson Githuka", 30, "Mathematics and Computer Science")
me.scholarship("Columbia","USA")

print(me.name)
print(me.course)
print(me.age)
print(me.varsity)
print(me.course)


