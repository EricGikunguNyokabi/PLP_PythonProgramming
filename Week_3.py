# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# print("PART 1 ")
def calculate_discount(price, discount_percent):
    price2 = price * (100-discount_percent)/100
    if discount_percent >= 20:
        return price2
    else:
        return price


# print("PART 2 ")
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.
price = float(input("Enter the original price : "))
discount_percent = float(input("Enter the discount percentage : "))

print(calculate_discount(price,discount_percent))

