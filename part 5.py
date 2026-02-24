#Challenge 1
numbers = input("What's your mobile phone numbers? ").strip()

import re

if re.search(r"^(07\d{8,12}|447\d{7,11})$", numbers):
    print("Valid")

else:
    print("Invalid")

#Challenge 2
id = input("What's your student ID? ").strip()

import re

if re.search(r"^[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][^\S]$", id):
    print("Valid")

else:
    print("Invalid")
