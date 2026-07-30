drink_prices = {
  "coffee": 4500,
  "tea": 2000,
  "lemonade": 3800
}

drink_prices_usd = {tea: price / 0.00031 for tea, price in drink_prices.items()}
print(drink_prices_usd)