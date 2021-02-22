import re


message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 for my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # \d regex for digit
mo = phoneNumRegex.search(message) # find the first match 
print(mo.group())

#print(phoneNumRegex.findall(message)) #find all the string that is match with regex

