import csv

contacts = open("contacts.csv", newline='')

contact = csv.DictReader(contacts)

for i in contact:
    print(i["name"] + "," + i["email"])

contacts.close()




