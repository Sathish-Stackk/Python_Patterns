password = input("Enter password: ")

valid = (
    len(password) >= 8
    and any(ch.isdigit() for ch in password)
    and any(ch.isupper() for ch in password)
)

print("Strong Password" if valid else "Weak Password")
