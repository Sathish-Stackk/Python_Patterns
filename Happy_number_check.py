def is_happy_number(number):
    visited = set()

    while number != 1 and number not in visited:
        visited.add(number)

        number = sum(int(digit) ** 2 for digit in str(number))

    return number == 1


num = int(input("Enter a number: "))

if is_happy_number(num):
    print(f"{num} is a Happy Number 😊")
else:
    print(f"{num} is not a Happy Number ❌")
