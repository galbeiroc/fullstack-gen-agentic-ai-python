drink_prices = {
  "coffee": 4500,
  "tea": 2000,
  "lemonade": 3800
}

drink_prices_usd = {drink: price / 0.00031 for drink, price in drink_prices.items()}
print(drink_prices_usd)

devices = {
  "computers": 2800,
  "phones": 1900,
  "printers": 1000,
  "tablets": 1500
}

discount_devices = {device: price * 0.1 for device, price in devices.items()}
print(discount_devices)