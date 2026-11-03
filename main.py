
def count_failed_logins(filename):

    attempts = {}

    with open(filename, "r") as file:
      for line in file:

          if "FAILED" in line:
              data = line.split(" ")
              ip = data[2].split("=")[1]

              if ip in attempts:
                  attempts[ip] += 1
              else:
                  attempts[ip] = 1
      return attempts

def display_report(attempts):
    threshold = 3
    print("Failed login summary:")
    for ip in attempts:
        print(ip, ":", attempts[ip], "failed attempts")

    print("\nSuspicious IPs:")

    for ip in attempts:
        if attempts[ip] >= threshold:
            print(ip)

filename = "sample.log"
attempts = count_failed_logins(filename)
display_report(attempts)
