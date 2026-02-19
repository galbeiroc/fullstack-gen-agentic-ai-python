cpu_usage = 85

if cpu_usage > 90:
  print("Alert: Critical usage!")
elif cpu_usage > 70:
  print("Warning: High usage!")
else:
  print("OK: CPU usage is normal.")