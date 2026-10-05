
""" 
This program analyzes a sentence entered by the user.
 It displays the sentence length, uppercase and lowercase 
versions, the first and last characters, the first and last
 5 characters, and the reversed sentence. Example: 

 
Input: Python is very powerful 

Output: 
Original: Python is very powerful 
Length: 24 
Upper: PYTHON IS VERY POWERFUL 
Lower: python is very powerful 
First Character: P 
Last Character: l 
First 5 Characters: Pytho 
Last 5 Characters: rful 
Reversed: lufrewop yrev si nohtyP

 """

Sentence = input("Enter a sentence of your choice for analysis: ")


print(Sentence)
print(f"Length: {len(Sentence)}")
print(f"Upper: {Sentence.upper()}")
print(f"Lower: {Sentence.lower()}")
print(f"First Character: {Sentence[0]}")
print(f"Last Character: {Sentence[-1]}")
print(f"First 5 Characters: {Sentence[:5]}")
print(f"Last 5 Characters: {Sentence[-5:]}")
print(f"Reversed: {Sentence[::-1]}")