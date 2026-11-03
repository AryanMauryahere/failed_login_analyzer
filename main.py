
import sys
import ipaddress

def extract_ip(line):
    data = line.split()

    for item in data:
        if item.startswith("ip="):
            ip = item.split("=", 1)[1]

            try:
                ipaddress.ip_address(ip)
                return ip
            except ValueError:
                return None
    return None

def count_failed_logins(filename):
    attempts = {}

    try:
        with open(filename, "r") as file:
            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                if not line.startswith("FAILED"):
                    continue

                ip = extract_ip(line)

                if ip is None:
                    print(f"Skipping malformed entry on line {line_number}")
                    continue

                if ip in attempts:
                    attempts[ip] += 1
                else:
                    attempts[ip] = 1

    except FileNotFoundError:
        print("Error: Log file not found!")
        return {}
    return attempts

def display_report(attempts):
    threshold = 3
    print("\nFailed login summary:")

    for ip in attempts:
        print(ip, ":", attempts[ip], "failed attempts")

    print("\nSuspicious IPs:")

    for ip in attempts:
        if attempts[ip] >= threshold:
            print(ip)


if len(sys.argv) < 2:
    print("Usage: python main.py <log_file>")
    sys.exit(1)

filename = sys.argv[1]
attempts = count_failed_logins(filename)
display_report(attempts)

with open("report.txt" , "w") as report_file:
    report_file.write("Failed login summary:\n")
    for ip in attempts:
        report_file.write(f"{ip} : {attempts[ip]} failed attempts\n")

    report_file.write("\nSuspicious IPs:\n")
    for ip in attempts:
        if attempts[ip] >= 3:
            report_file.write(f"{ip}\n")