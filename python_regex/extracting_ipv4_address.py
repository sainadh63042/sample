import re

text = "The server's IPv4 addresses are 192.168.1.1 and 10.0.0.1."
ipv4_pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b'

ipv4_addresses = re.findall(ipv4_pattern, text)
print(ipv4_addresses)
