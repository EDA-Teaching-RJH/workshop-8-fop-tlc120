email = input("What's your email? ").strip()

username, domain = email.split("@")

import re

if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.ac.uk$", email):
    print("Valid")

elif re.search(r"^[^@]+@[^@]+\.ac.uk$", email):
    print("Valid")

else:
    print("Invalid")