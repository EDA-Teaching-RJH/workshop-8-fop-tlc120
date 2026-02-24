email = input("What's your email? ").strip()

username, domain = email.split("@")

import re

if re.search(r"^\w+@\w.+\.(ac.uk | gov.uk | nhs.net)$", email):
    print("Valid")

else:
    print("Invalid")