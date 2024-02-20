# import re
#
# # Regular expression pattern to match a broader set of email addresses
# pattern = r'[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Z|a-z]+'
#
# text = "john123@example.com My email addresses are john123@example.com, alice@gmail.com, and bob@example.co.uk."
#
# # Using re.findall to find all matches
# matches = re.match(pattern, text)
# print(matches)
# if matches:
#     print("found")
# else:
#     print("Not found")
# # # Print the matches
# # for match in matches:
# #     print("Found email:", match)
import re

# Regular expression pattern to match IPv4 addresses
# ipv4_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ipv4_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

text = "IP addresses in the text are 192.168.0.1 and 10.0.0.255."

# Using re.findall to find all matches
matches = re.findall(ipv4_pattern, text)

# Print the matches
for match in matches:
    print("Found IPv4 address:", match)
