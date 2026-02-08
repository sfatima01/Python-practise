#program1:creating a tuple
numbers = (10, 20, 30, 40)
print(numbers)

#program2:elements in tuple
fruits = ("apple", "banana", "mango")
print(fruits[0])
print(fruits[-1])

#program3:looping and tuple
for fruit in fruits:
    print(fruit)
  
#program4:checking item in tuple
if "apple" in fruits:
    print("Apple is present")

#program5:mixed data tuple
person = ("Shakira", 18, "Python")
print(person)

#program6:accesing data
name, age, course = person
print(name)
print(age)
print(course)
