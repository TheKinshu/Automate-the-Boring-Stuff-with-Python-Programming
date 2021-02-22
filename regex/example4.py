import re


# Using a '?' allow you to match 0 to 1 times while a '*' matches from 0 to more
# '+' allow you to match 1 or more
# To find special character like '?' or '+' you can use '\' backslash to escape
batRegex = re.compile(r'Bat(wo)?man') # Same as b'Batman|Batwoman'

mo = batRegex.search('The Adventures of Batman')
print(mo.group()) # Batman


mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # Batwoman


mo = batRegex.search('The Adventures of Batwowowoman')
if mo != None:
    print(mo.group())
else:
    print("Found nothing") # mo is empty

phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
phoneRegex.search('Call me 415-555-1011 tomorrow')

haRegex = re.compile(r'(Ha){3}')

# The '{}' allow you to specify the amount of time you want it to match
# {3, 5} 3 is the minimum and 5 is the max number it will find
mo = haRegex.search('He said "HaHaHa"')
print(mo) # HaHaHa

# By default python does greedy matches so it will match with the maximum number of string
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('123456789')
print(mo) # 12345

# To do a non-greedy match add a '?' after the '5}'
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('123456789')
print(mo) # 123
