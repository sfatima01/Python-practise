#day3:loops practice
#program1:print numbers from 1 to 5
for i in range(1, 6):
    print(i)
    
  #program2:print even numbers from 1 to 20
for  i in range(1, 21):
    if i % 2 == 0:
        print(i)

#program3:sum of first N numbers
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("Sum is:", total)

#program4:multiplication table 
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

#program5:while loop example
i = 1
while i <= 5:
    print("Hello")
    i += 1
