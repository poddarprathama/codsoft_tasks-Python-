# Get password length
length = int(input("Enter password length: "))

# Character set
chars = "abcdeABCDE12345@#$%"

password = ""
i = 0

# Generate password
while i < length:
    password = password + chars[(i + length) % len(chars)]
    i = i + 1

# Show result
print("Your Password is:", password)




