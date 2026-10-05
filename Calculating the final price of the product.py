

"""
This program calculates the total price of a product based on its price
and selling quantity. It then calculates the discount amount and the
final payable amount after applying the discount.

Example:
Input:
Product name: Chocolate
Product price: 50
Product selling quantity: 4
Product discount: 10

Output:
--------------------Factor---------------------
Product name: Chocolate
Product price: 50.0
Product selling quantity: 4
Product discount is 10.0% and Product discount price is 20.0
-----------------------------------------------
Amount payable after discount: 180.0
-----------------------------------------------
"""


ProductName = input("Enter the product name: ")
ProductPrice = float(input("Enter product price: "))
ProductQuantity = int(input("Enter product selling quantity: "))
ProductDiscount = float(input("Enter product discount: "))


TotalPrice = ProductPrice * ProductQuantity
DiscountPrice = (TotalPrice * ProductDiscount) / 100

print("--------------------Factor---------------------")
print(f"Product name:  {ProductName}")
print(f"Product price:  {int(ProductPrice)}")
print(f"Product selling quantity:  {ProductQuantity}")
print(f"Product discount is {int(ProductDiscount)}% and Product discount price is {int(DiscountPrice)}")
print("-----------------------------------------------")
print(f"Amount payable after discount:  {int(TotalPrice - DiscountPrice)}")
print("-----------------------------------------------")