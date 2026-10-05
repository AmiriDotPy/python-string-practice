"""
Algorithm:
1. Store the product code in a string.
2. Use indexing and slicing to extract each part of the code.
3. Extract:
   - First 2 characters as the country.
   - Characters 3 to 5 as the city.
   - Characters 7 to 8 as the year.
   - Characters 10 to 12 as the price.
   - Characters 14 and onward as the size.
4. Display each extracted value with a descriptive label.

Example Input:
Product code: IR-ARD-95-500-XL

Full Output:
Country: IR
City: ARD
Year: 95
Price: 500
Size: XL
"""


product_code = "IR-ARD-95-500-XL"

print(f"    Country: {product_code[:2]}")
print(f"    City: {product_code[3:6]}")
print(f"    Year: {product_code[7:9]}")
print(f"    Price: {product_code[10:13]}")
print(f"    Size: {product_code[14:]}")
