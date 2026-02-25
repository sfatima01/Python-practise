#program 1:basic inputs
name = input("Enter your name: ")
print("Hello", name)

#program 2:input age
age = int(input("Enter your age: "))
print("Your age is", age)

#program 3:largest among two
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a > b:
    print("Largest:", a)
else:
    print("Largest:", b)

#program 4:addition
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum =", a + b)

#program 5:even or odd
n = int(input("Enter number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

#program 6:multiplication
n = int(input("Enter number: "))

for i in range(1, 15):
    print(a, "x", i, "=", a * i)

#program 7:student grades
marks = int(input("Enter marks: "))

if marks >= 90:
  print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
