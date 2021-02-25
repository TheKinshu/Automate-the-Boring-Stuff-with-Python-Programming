# pip install imapclient
# pip install pyzmail36

# Provider              |IMAP server Domain name
#-----------------------|------------------------
# Gmail                 |imap.gmail.com
# Outlook/Hotmail.com   |imap-mail.outlook.com
# Yahoo Mail            |imap.map.yahoo.com
# AT&T                  |imap.mail.att.net
# Comcast               |imap.comcast.net
# Verizon               |incoming.verizon.ney


# Search keys
# All

# BEFORE 'DATE'
# ON     'DATE'
# SINCE  'DATE'

# SUBJECT 'STRING'
# BODY    'STRING'
# TEXT    'STRING'

# For more search terms visit:
# http://www.marshallsoft.com/ImapSearch.htm

import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('youremail@gmail.com', 'khkhycskynqmiyiv')

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE', '21-Dec-2020'])
print(UIDs)

rawMessage = conn.fetch([2799], ['BODY[]', 'FLAGS'])

message = pyzmail.PyzMessage.factory(rawMessage[2799][b'BODY[]'])

# message.get_subject() get subject of the message
# message.get_adresses('from') // to, bcc(blank carbon copy)

# These check if the email has image or not.
# They both return True or False depending on the email 
# message.text_part 
# message.html_part

print(message.text_part.get_payload().decode('UTF-8'))






conn.logout()