numbers = [12, 5, 8, 12, 7, 5, 20, 8, 9]

duplicates = []

for number in numbers:
    if numbers.count(number) > 1 and number not in duplicates:
        duplicates.append(number)

print("Duplicates:", duplicates)
