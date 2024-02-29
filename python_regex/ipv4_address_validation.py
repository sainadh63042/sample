import re

def is_valid_ipv4(ip):
    ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    if re.fullmatch(ipv4_pattern, ip):
        return True
    else:
        return False

ip_address = "192.168.1.1"
if is_valid_ipv4(ip_address):
    print(f"{ip_address} is a valid IPv4 address.")
else:
    print(f"{ip_address} is not a valid IPv4 address.")
