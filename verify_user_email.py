import re

pattern = "[a-zA-Z0-9] +@ [a-zA-Z]+\.(com|edu|net)"

Uinput = input("Enter your email: ")
if re.search(pattern, Uinput):
    print("Valid email")
else:
    print("Invalid email")

