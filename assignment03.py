#FUNCTIONS IN PYTHON
price = int(input("Enter the original price of the product here: "))
discount_percent = int(input("If given discount, enter value here: "))

def calculate_discount (price, discount_percent):
    if discount_percent >= 20:
        calculation = int(price - (price * discount_percent / 100))
        print(f"TOTAL PRICE: {calculation}")
    else:
        print(f"TOTAL PRICE: {price}")

calculate_discount(price,discount_percent)
