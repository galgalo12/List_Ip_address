  This Python script performs the following tasks:

  Defines a list of known malicious IP addresses: Malicious_Ipaddress contains IPs identified as malicious.

  Sorts and displays these malicious IPs: It prints the Malicious_Ipaddress list in ascending order.

  Lists all login attempt IPs: ip_addresses represents IPs attempting to log in.

  Prints each login attempt IP: Iterates through ip_addresses and prints each IP.

  Defines an allowed list of IP addresses: allow_list contains IPs permitted to access the system.

  Checks each login attempt against the allowed list:

If an IP is in allow_list, it prints that the IP is allowed.

If an IP is not in allow_list, it increments the malicious IP count and prints a warning to block the IP in the firewall.

Displays the total number of malicious IP addresses detected: Prints the count of IPs that should be blocked.
