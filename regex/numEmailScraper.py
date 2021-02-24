#! python3

# Developing a program that scrape documentation that for multiple phone numbers and email addresses

import re, pyperclip

# Create a Regex for phone numbers
phoneRegex = re.compile(r'''
                        (((\d\d\d)|(\(\d\d\d\)))?  # Area code (optional) 000
                        (\s|-)                     # First separator (If area code is not available look for whitespace or dash)
                        \d\d\d                     # First 3 digit        000
                        -                          # Second separator
                        \d\d\d\d                   # Last 4 digit         0000
                        (((ext(\.)?\s) | x)        # Extension word/character (optional: This check if the extension is using 'ext' or 'x')
                        (\d{2,5}))?)               # Extension numbers (optional: check if theres 2 or more character)
                        ''', re.VERBOSE)

# Create a Rregex for email address
emailRegex = re.compile(r'''
                         [a-zA-Z0-9_.+]+           # Email name
                         @                         # @ symbol
                         [a-zA-Z0-9_.+]+           # Domain name
                         ''', re.VERBOSE)

# Get the text off the clipboard
text = pyperclip.paste()

# Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

# Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)