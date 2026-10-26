password = input("Enter your password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters")

if not any(c.isupper() for c in password):
    print("Add an uppercase letter")

if not any(c.islower() for c in password):
    print("Add a lowercase letter")

if not any(c.isdigit() for c in password):
    print("Add a digit")

if not any(not c.isalnum() for c in password):
    print("Add a special character")

if (
    len(password) >= 8
    and any(c.isupper() for c in password)
    and any(c.islower() for c in password)
    and any(c.isdigit() for c in password)
    and any(not c.isalnum() for c in password)
):
    print("Password is valid")
else:
    print("Password is invalid")
