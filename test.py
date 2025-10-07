
numbers = [10, 15, 20, 25, 30, 35, 40]

print(*numbers[::2])

print(*[num for num in numbers if num % 2 ==0])

print([num for i, num in enumerate(numbers) if num % 2 == 0])
