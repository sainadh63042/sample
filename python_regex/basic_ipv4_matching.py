import re

text = "192.168.1.1 is the IPv4 address of the router."
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

ipv4_addresses = re.findall(ipv4_pattern, text)
print(ipv4_addresses)
