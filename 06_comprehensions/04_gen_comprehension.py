daily_sales = [5, 10, 12, 28, 4, 8, 15, 9]

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups) # 82
