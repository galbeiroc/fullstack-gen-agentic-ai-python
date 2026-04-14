def get_discount(customer_type):
    if customer_type == "regular":
        return 0.1
    elif customer_type == "vip":
        return 0.2
    else:
        return 0.0