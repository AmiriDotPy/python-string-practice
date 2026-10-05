
""" 
This program creates a user ID using
the user's first name, last name, birth 
year, and city.Names and city are converted
to lowercase. The first 3 letters of the 
last name and city, and the last 2 digits oب
 the birth year are used. 
 
 Example: Input: Mahyodin, Amiri, Ardabil, 1995 
 Output: mahyodin.ami95.ard 
 """


Fname = input("Enter your first name:").lower()
Lname = input("Enter your last name:").lower()
City = input("Enter your city name:").lower()
YearOfBirth = input("Enter your year of birth:")


print(f"{Fname}.{Lname[:3]}{YearOfBirth[-2:]}.{City[:3]}")