#program1:simple functions
def greet():
    print("hi! ")

greet()
greet()

#program2:functions with parameter
def greet(name):
    print("Hello", name)

greet("Shakira")
greet("Python")

#program3:function with return value
def add(x, y):
    return x + y

result = add(6,8)
print("Sum:", result)

#program4:even or odd function
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print(even_or_odd(10))
