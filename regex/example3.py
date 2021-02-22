import re


message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)') # \d regex for digit
mo = phoneNumRegex.search(message) # find the first match 
print(mo.group(1)) # adding brackets can group the regex and allow you to find a specific group by using numbers


batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel')
print(mo.group())
