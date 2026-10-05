"""
Algorithm:
1. Split the complete input string using "|" as the main separator.
2. Extract the name, age, city, job, and birth year using list indexes.
3. Use strip() to remove extra spaces around each extracted value.
4. Split the full name into first name and last name.
5. Convert the age to an integer and calculate the age for next year.
6. Calculate the name length and create uppercase/lowercase versions.
7. Create a username using the lowercase first name, lowercase last name,
   and the last two digits of the birth year.

Example Input:
Mohyaldin Amiri | 31 | Ardabil | Python Developer | 1995

Full Output:
========== USER REPORT ==========
Name: Mohyaldin Amiri
First Name: Mohyaldin
Last Name: Amiri

Age: 31
Birth Year: 1995
Age Next Year: 32

City: Ardabil
Job: Python Developer

Name Length: 15
Upper Name: MOHYALDIN AMIRI
Lower Job: python developer

Username: mohyaldin.amiri95
"""

info = "Mohyaldin Amiri | 31 | Ardabil | Python Developer | 1995".split("|")

print("========== USER REPORT ==========")
print(f"Name: {info[0].strip()}")
print(f"First Name: {info[0].split(' ')[0].strip()}")
print(f"Last Name: {info[0].split(' ')[1].strip()}\n")

print(f"Age: {info[1].strip()}")
print(f"Birth Year: {info[4].strip()}")
print(f"Age Next Year: {int(info[1]) + 1}\n")

print(f"City: {info[2].strip()}")
print(f"Job: {info[3].strip()}\n")

print(f"Name Length: {len(info[0].strip())}")
print(f"Upper Name: {info[0].upper().strip()}")
print(f"Lower Job: {info[3].lower().strip()}\n")

print(f"Username: {info[0].split(' ')[0].lower().strip()}.{info[0].split(' ')[1].lower().strip()}{info[4][-2:].strip()}")