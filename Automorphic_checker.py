def is_automorphic(number):
    square = number ** 2

    return str(square).endswith(str(number))


num = int(input("Enter a number: "))

if is_automorphic(num):
    print(f"{num} is an Automorphic Number")
else:
    print(f"{num} is not an Automorphic Number")
