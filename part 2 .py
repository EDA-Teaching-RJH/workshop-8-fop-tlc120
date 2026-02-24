email = input("What's your email? ").strip()

username, domain = email.split("@")

import re

if re.search(r".+@.+\.ac.uk", email):
    print("Valid")

else:
    print("Invalid")