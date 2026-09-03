from functools import wraps

def log_activity(func):
  @wraps(func)
  def wrapper(*args, **kwargs):
    print(f"🚀 Calling: {func.__name__}")
    result = func(*args, **kwargs)
    print(f"✅ Finish {func.__name__}")
    return result
  return wrapper

@log_activity
def brew_drink(type, milk="no"):
  print(f"Brewing {type} drink and milk status {milk}")

brew_drink("Coffee")