import re

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# sub find and replace base on the regex pattern
mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)


# (\w)\w* This regex finds the name of the agent but also group the first character -
# of the name for later usage.
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# Instead of using REDACTED, the following sub uses the first character -
# of the Agent name as code and adds * after for added effects.
mo = namesRegex.sub(r'Agent \1****', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# Verbose function allow you to create a more complicated and readable regex
# By separating them into multiple lines it creates a more readable regex and -
# allowing you to add documentation inbetween them each lines.
re.compile(r'''(\d\d\d-)|       # Area code (without parens)
               (\(\d\d\d\) )     # Area code (with parens and no dash)
               \d\d\d-          # First 3 digit
               \d\d\d\d         # Last 4 digit
               \sx\d{2,4} ''',  # Extension, like x1234
               re.VERBOSE)      # To add more extension feature like IGNORECASE or DOTALL you can implement them by using the '|' 
                                # ex. (re.VERBOSE | re.DOTALL | re.IGNORECASE)

