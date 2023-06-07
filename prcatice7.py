
numbers = []
finish = False
while not finish:
    user_input = input("Enter a number: ")
    if user_input == 'done':
        squares = sorted([n ** 2 for n in numbers])
        even = [n for n in numbers if n % 2 == 0]
        print(f"Maximum: {max(numbers)}")
        print(f"Minimum: {min(numbers)}")
        print(f"Sum: {sum(numbers)}")
        print(f"Squares: {squares}")
        print(f"Even numbers: {len(even)}")
        break
    else:
        numbers.append(int(user_input))


