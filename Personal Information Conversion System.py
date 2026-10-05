"""
Algorithm:
1. Get the user's full name, age, city, and job.
2. Remove extra spaces from text inputs and convert them to lowercase.
3. Convert age to an integer so it can be used in calculations.
4. Create a professional introduction using an f-string.
5. Calculate the user's age next year by adding 1 to the current age.
6. Use title() to display the name, city, and job in title case.

Example Input:
Enter your full name: Mohyaldin Amiri
Enter your age: 31
Enter your city name: Ardabil
Enter your job: marketer

Full Output:

    My name is Mohyaldin Amiri.

    I am 31 years old and next year I will be 32.

    I live in Ardabil.

    I work as a Marketer.
"""

full_name = input("Enter your full name: ").strip().lower()
age = int(input("Enter your age: "))
city = input("Enter your city name: ").strip().lower()
job = input("Enter your job: ").strip().lower()


full_info = f'''
    My name is {full_name.title()}.
    I am {age} years old and next year I will be {age+1}.
    I live in {city.title()}.
    I work as a {job.title()}.
'''


print(full_info)