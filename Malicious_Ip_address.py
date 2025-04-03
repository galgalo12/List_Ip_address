# List of known malicious IP addresses
Malicious_Ipaddress = [
    "192.168.142.245", "192.168.109.50", "192.168.86.232",
    "192.168.131.147", "192.168.205.12", "192.168.200.48"
]

# Sort and display failed login attempts in ascending order
print("Sorted failed login attempts:", sorted(Malicious_Ipaddress))
print("\n")

# List of login attempt IPs
ip_addresses = [
    "192.168.142.245", "192.168.109.50", "192.168.86.232", 
    "192.168.131.147", "192.168.205.12", "192.168.200.48"
]

# Print all login attempt IPs
print("Malicious Login Attempt IPs:\n")
for ip in ip_addresses:
    print(ip)
print("\n")

# Allowed list of IP addresses
allow_list = [
    "192.168.243.140", "192.168.205.12", "192.168.151.162", 
    "192.168.178.71", "192.168.86.232", "192.168.3.24", 
    "192.168.170.243", "192.168.119.173"
]

# Counter for malicious IP addresses
malicious_count = 0

# Check if login attempt IPs are allowed or should be blocked
for ip in ip_addresses:
    if ip in allow_list:
        print(f"✅ {ip} - This IP address is allowed.\n")  # Allowed IPs
    else:
        malicious_count += 1  # Increment malicious IP count
        print(f"⛔ {ip} - This IP is malicious and has been BLOCKED by the firewall.\n")  # Malicious IPs

# Print the total count of malicious IP addresses
print(f"🚨 Total malicious IP addresses detected and blocked: {malicious_count}")
