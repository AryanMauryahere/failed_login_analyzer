file = open("sample.log", "r")

attempts = {}
treshold = 3

for line in file:
  if "FAILED" in line:
    result = line.split(" ")
    # print(result[2].split("=")[1])
    ip = result[2].split("=")[1]

    if ip in attempts:
      attempts[ip] += 1
    else:
      attempts[ip] = 1

    # if attempts[ip] >= treshold:
    #   print(f"IP address {ip} has exceeded the threshold of {treshold} failed login attempts.")
    # else:
      # print(f"IP address {ip} has {attempts[ip]} failed login attempts.")

file.close()

print("Failed login attempts by IP address:")
for ip in attempts:
  print(f"{ip}: {attempts[ip]} attempts")

for ip in attempts:
  if attempts[ip] >= treshold:
    print(f"Suspicious IP addresses : {ip}")