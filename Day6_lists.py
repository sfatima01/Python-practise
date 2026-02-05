#program1:making a list
numbers = [1, 2, 3, 4, 5]
print(numbers)

#program2:accessing elements
fruits = ["watermelon", "peach", "mango"]
print(fruits[0])
print(fruits[-1])

#program3:sum of list
nums = [10, 20, 30]
print(sum(nums))

#program4:largest number and smallest number in list
nums = [5, 12, 9]
print(max(nums))
print(min(nums)) 

#program5:input numbers
numbers = []
for i in range(5):
    num = int(input("Enter number: "))
    numbers.append(num)
print("Your list:", numbers)

#program6:even number from list
nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n%2==0:
        print(n, "is even")

#program7:reversing a list
nums = [1, 2, 3, 4]
nums.reverse()
print(nums)

#program8:lenght of list
print("Total fruits:", len(fruits))
