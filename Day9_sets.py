#program1:create set
numbers = {1, 2, 3, 4, 4, 5}
print(numbers)

#program2:add and delete
numbers.add(6)
numbers.remove(2)
print(numbers)

#program3:checking item exists
if 3 in numbers:
    print("3 is present")

#program4:union of elements
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

#program4:intersection of terms
print(a & b)

#program5:removing duplicate from list
nums = [1, 2, 2, 3, 4, 4]
unique_nums = set(nums)
print(unique_nums)

program6:converting set into list
unique_list = list(unique_nums)
print(unique_list)
