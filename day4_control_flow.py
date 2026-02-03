#Program1: Stop at number entered by user
num = int(input("Enter a number: "))

for i in range(1, 11):
    if i == num:
        break
    print(i) 
  
  #program2:skip even numbers

  for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
    
  #Program3: Square pattern
for i in range(4):
    for j in range(4):
        print("*", end=" ")
    print()
  
    #Program4: Number pattern
for i in range(1, 5):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
  
#Program 5: Triangle star pattern

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()
