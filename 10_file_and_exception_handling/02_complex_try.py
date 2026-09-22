def serve_drink(flavor):
  try:
    print(f"Preparing {flavor} drink...")
    if flavor == "unknown":
      raise ValueError("We dont know this flavor")
  except ValueError as e:
    print("Error: ", e)
  else:
    print(f"{flavor} drink served")
  finally:
    print("Next customer please...")

serve_drink("coffee")
serve_drink("unknown")