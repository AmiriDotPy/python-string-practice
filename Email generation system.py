
"""
This program creates an email address using the user's first name,
last name, and birth year. Extra spaces are removed from the names,
letters are converted to lowercase, the first 5 characters of the
last name are used, and the last 2 digits of the birth year are added.

Example:
Input:
First name: Mohyaldin
Last name: Amiri
Birth year: 1995

Output:
Email Address: mohyaldin.amiri95@gmail.com
"""



FirstName = input("Enter your first name: ").strip().lower()
LastName = input("Enter your last name: ").strip().lower()
BirthYear = input("Enter your Birth Year: ")

print(f"Email Address: {FirstName}.{LastName[:5]}{BirthYear[-2:]}@gmail.com")