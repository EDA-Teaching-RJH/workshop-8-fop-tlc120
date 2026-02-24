email = input("What's your email? ").strip()

username, domain = email.split("@")
if username and domain.endswith(".ac.uk"):
    print("Valid")

else:
    print("Invalid")