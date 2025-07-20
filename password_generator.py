import random
import string

print("----- Password Generator -----")

# Step 1: Take password length from user
length = int(input("Enter desired password length: "))

# Step 2: Define character sets
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Step 3: Combine all characters
all_characters = lowercase + uppercase + digits + symbols

# Step 4: Generate password
password = ''.join(random.choice(all_characters) for i in range(length))

# Step 5: Show password
print("Generated Password:", password)
