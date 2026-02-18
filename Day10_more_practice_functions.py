program6:largest of two numbers
def largest(a, b):
    if x > y:
        return x
    else:
        return y

print(largest(20, 30))

program7:adittion of list
def sum_list(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

nums = [10, 29, 38]
print(sum_list(nums))

program8:vowels counting
def count_vowels(text):
    count = 0
    vowels = "aeiouAEIOU"
    
    for ch in text:
        if ch in vowels:
            count += 1
            
    return count

print(count_vowels("Python Programming"))

program9:calculator function
def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return "Invalid"

print(calculator(10, 6, "+"))
print(calculator(10, 6, "*"))

program10:function calling function
def square(n):
    return n * n

def show_square(x):
    print("Square is:", square(x))

show_square(6)
