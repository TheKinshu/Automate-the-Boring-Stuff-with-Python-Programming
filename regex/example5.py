import re

# '^' This matches string that starts with Hello
beginsWithHelloRegex = re.compile(r'^Hello')

mo = beginsWithHelloRegex.search('Hello there!')

print(mo)

# This returns none because Hello is not at the beginning of the string
mo = beginsWithHelloRegex.search('He said "Hello!"')

print(mo)

# '$' This check the strings if it ends with world!
endsWithWorldRegex = re.compile(r'world!$')
mo = endsWithWorldRegex.search('Hello world!')
print(mo)

# This returns none because world! is not at the end of the string
mo = endsWithWorldRegex.search('Hello world! asdfasedf')
print(mo)

# r'^both$' This regex must match the entire string
allDigitsRegex = re.compile(r'^\d+$')
mo = allDigitsRegex.search('324235235')
print(mo)

# 'x' is not a digit but the pattern is looking for only -
# digit so this will return none 
mo = allDigitsRegex.search('32423x5235')
print(mo)

# '.' matches any character with the following same pattern
# ex. (r'.at') This will match with any things that has have ends with at
# The cat in the hat sat on the flat mat.
# Only cat, hat, sat, lat, and mat will be matched. flat was not fully matched because -
# the '.' was only looking for a singluar character.

# r'.*' This regex will match with any character 0 to more times
# This greedy version only work up to the new-line

# To do a non-greedy match with match all is by adding a '?' after the '*'
# ex: r'<(.*?)>'
# This will up until the first '>'

# One way to by pass new-line for '.*' is by doing the following:
# re.compile(r'.*', re.DOTALL)
# This will cause it to match the entire strings ignore the new-line exception

# using re.I or re.IGNORECASE can ignore any case sensitive from the matches
