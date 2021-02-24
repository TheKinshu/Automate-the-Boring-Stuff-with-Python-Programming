import webbrowser, sys, pyperclip

sys.argv # ['webMod.py', '870', 'Valencia', 'St.']

# Check if command line arguments were passed

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste() 

# https://www.google.com/maps/place/<ADDRESS>
# opens the web browser based on what the user input or has copy
webbrowser.open('https://www.google.com/maps/place/' + address)
