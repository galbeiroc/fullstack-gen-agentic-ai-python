def generate_bill(coffee, tax):
    """
    This function calculates the total bill for a cup of coffee, including tax.

    Parameters:
    coffee (float): The price of the coffee.
    tax (float): The tax amount to be added to the coffee price.

    Returns:
    float: The total bill including the tax.
    """
    bill = coffee + tax
    return bill

print(generate_bill(3.50, 0.50))  # Output: 4.0
print(generate_bill.__doc__)
print(generate_bill.__name__)