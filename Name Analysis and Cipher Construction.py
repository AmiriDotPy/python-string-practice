"""
Algorithm:
1. Get the user's full name and split it into first name and family name.
2. Get the user's birth year as a string.
3. Display the first name, family name, and their lengths.
4. Convert the first name to uppercase and the family name to lowercase.
5. Reverse the first name using slicing.
6. Create a sample password using the first 4 characters of the reversed name,
   the first 2 characters of the family name in uppercase, and the last 2 digits
   of the birth year.

Example Input:
Enter your name and family: mohyaldin amiri
Enter your birth year: 1995

Full Output:
>>>>Name:...........>|mohyaldin|
>>>>Famili:.........>|amiri|
>>>>Name Length:....>|9|
>>>>Family Length:..>|5|
>>>>Upper Name:.....>|MOHYALDIN|
>>>>Lower Family:...>|amiri|
>>>>Reverse Name:...>|nidlayhom|
>>>>Password:.......>|nidlAM95|
"""

name = input("Enter your  name and family : ").split()
birth_year = input("Enter your birth year: ")


print(f">>>>Name:...........>|{name[0]}|")
print(f">>>>Famili:.........>|{name[1]}|")
print(f">>>>Name Length:....>|{len(name[0])}|")
print(f">>>>Family Length:..>|{len(name[1])}|")
print(f">>>>Upper Name:.....>|{name[0].upper()}|")
print(f">>>>Lower Family:...>|{name[1].lower()}|")
print(f">>>>Reverse Name:...>|{name[0][::-1]}|")
print(f">>>>Password:.......>|{name[0][::-1][:4]}{name[1][:2].upper()}{birth_year[-2:]}|")

