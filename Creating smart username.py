"""
Algorithm:
1. Get the user's first name, last name, and birth year.
2. Remove extra spaces and convert the names to lowercase.
3. Create a full information string and display it in title case.
4. Build the username using:
   - First 3 characters of the first name.
   - Last 3 characters of the last name.
   - Last 2 digits of the birth year.

Example Input:
Enter your first name: Mohyaldin
Enter your last name: Amiri
Enter your birth year: 1995

Full Output:
============full info============
Mohyaldin Amiri 1995
============user name============
mohiri95
=================================
"""


first_name = input("Enter your first name: ").strip().lower()
last_name = input("Enter your last name: ").strip().lower()
birth_year = input("Enter your birth year: ").strip()

full_info = f"{first_name} {last_name} {birth_year}"

print("============full info============")
print(full_info.title())
print("============user name============")
print(f"{first_name[:3]}{last_name[-3:]}{birth_year[-2:]}")
print("=================================")