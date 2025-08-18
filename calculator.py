def calculate_discount(price, discount_percent):
    """Calculate final price after applying discount if it's >= 20%."""
    if discount_percent >= 20:
        discount_amount = (price * discount_percent) / 100
        return price - discount_amount
    else:
        return price  # return original price if discount < 20%


# Prompt user for input
try:
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"Discount applied! Final price is: ${final_price:.2f}")
    else:
        print(f"No discount applied. Price remains: ${final_price:.2f}")

except ValueError:
    print("Invalid input. Please enter numeric values.")
